from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user.username} created successfully!")
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('user_login')







