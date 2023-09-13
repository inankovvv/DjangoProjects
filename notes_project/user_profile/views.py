from django.shortcuts import render, redirect
from user_profile.forms import UserForm, UserProfileInfoForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'user_profile/all_users.html')


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('notes_app:index'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('notes_app:index'))
            else:
                return HttpResponse('User not active!')
        else:
            return HttpResponse('User not found!')

    return render(request, 'user_profile/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('notes_app:index'))


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('notes_app:index'))

    registered = False
    user_form = UserForm()
    profile_form = UserProfileInfoForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            login(request, user)
            registered = True
            return HttpResponseRedirect(reverse('notes_app:index'))

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'user_profile/register.html', context)



