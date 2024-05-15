from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm


app_name = 'my_app'


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('my_app:home')
        else:
            messages.success(request, 'Invalid login credentials')
            return redirect('my_app:home')
    return render(request, 'my_app/home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('my_app:home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created for ' + username)
            return redirect('my_app:home')
    else:
        form = RegisterForm()
        return render(request, 'my_app/register.html', {'form': form})

    return render(request, 'my_app/register.html', {'form': form})




