import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.safestring import mark_safe

from users.models import User
from .forms import (
    RegisterForm,
    LoginForm,
    PasswordChangeForm,
    PasswordResetForm,
    SendPasswordResetEmailForm, ProfileForm)


def user_register(request):
    """
    Register a user
    """
    if request.user.is_authenticated():
        return redirect('home')

    form = RegisterForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            messages.success(request, mark_safe("You have sucessfully registered...<a href = '/users/login'>Click here to login</a>"))
            #login(request, user)
            return redirect('users:register')

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def user_login(request):
    """
    Login a user
    """
    next = request.GET.get('next', None)
    if request.user.is_authenticated():
        return redirect('home')

    form = LoginForm(data=request.POST or None)

    context = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Invalid login credentials")
                return render(request, 'users/login.html', context)
            else:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('home')

    return render(request, 'users/login.html', context)


def user_email_confirm(request):
    """
    Confirm user's email
    """
    if request.user.is_authenticated():
        return redirect('home')

    token = request.GET.get('token')
    if token is None:
        raise Http404()

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    except jwt.ExpiredSignature:
        messages.error(request, 'Confirmation token has expired.')
        return redirect('home')
    except jwt.DecodeError:
        messages.error(request, 'Error decoding confirmation token.')
        return redirect('home')
    except jwt.InvalidTokenError:
        messages.error(request, 'Invalid confirmation token.')
        return redirect('home')

    try:
        user = User.objects.get(pk=payload['confirm'])
    except User.DoesNotExist:
        messages.error(request, 'Account not found.')
        return redirect('home')

    if user.is_confirmed:
        messages.error(request, "Email already confirmed.")
    else:
        user.is_confirmed = True
        user.save()
        messages.success(request, "Email confirmed.")
    return redirect('users:login')


@login_required
def user_password_change(request):
    """
    Change user password
    """
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password changed successfully")
            return redirect('user_password_change')

    context = {
        'form': form
    }
    return render(request, 'users/change_password.html', context)


def user_send_password_reset_email(request):
    """
    Send password reset email
    """
    if request.user.is_authenticated():
        return redirect('home')

    form = SendPasswordResetEmailForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset email sent. Please check your email for instructions.")
            return redirect('users:send_password_reset_email')

    context = {
        'form': form
    }
    return render(request, 'users/send_password_reset_email.html', context)


def user_password_reset(request):
    """
    Reset user password
    """
    if request.user.is_authenticated():
        return redirect('home')

    token = request.GET.get('token')
    if token is None:
        raise Http404()

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithm='HS256')
    except jwt.ExpiredSignature:
        messages.error(request, 'Reset token has expired.')
        return redirect('users:send_password_reset_email')
    except jwt.DecodeError:
        messages.error(request, 'Error decoding reset token.')
        return redirect('users:send_password_reset_email')
    except jwt.InvalidTokenError:
        messages.error(request, 'Invalid reset token.')
        return redirect('users:send_password_reset_email')

    try:
        user = User.objects.get(pk=payload['reset'])
    except User.DoesNotExist:
        messages.error(request, 'Invalid token.')
        return redirect('users:send_password_reset_email')

    form = PasswordResetForm(data=request.POST or None, user=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Password reset successfully.")
            return redirect('users:login')

    context = {
        'form': form
    }
    return render(request, 'users/password_reset.html', context)


@login_required
def user_logout(request):
    """
    Logout a user
    """
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('users:login')


@login_required
def user_profile_edit(request):
    """
    Edit user profile
    """
    form = ProfileForm(instance=request.user, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('users:profile_edit')

    context = {
        'form': form
    }
    return render(request, 'users/profile_edit.html', context)
