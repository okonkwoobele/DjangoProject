from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from main.forms.forms import RegistrationForm, LoginForm


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('registration_successful')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form, 'register_success': False})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('login_success')
            else:
                return render(request, 'login.html', {'form': form, 'login_error': 'Invalid username or password.'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def login_success(request):
    return render(request, 'login_success.html')


def home(request):
    return render(request, 'home.html', {})


def registration_successful(request):
    return render(request, 'registration_successful.html')
