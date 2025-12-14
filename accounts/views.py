from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username , password=password)
            login(request , user)
            messages.success(request , f'Аккаунт {username} успешно создан!')
            return redirect('home')
        else:
            for field , errors in form.errors.items():
                for error in errors:
                    messages.error(request , f'{field}: {error}')
    else:
        form = UserCreationForm()

    return render(request , 'accounts/register.html')


def profile(request):
    return render(request , 'accounts/profile.html')
