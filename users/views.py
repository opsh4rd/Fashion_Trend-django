from django.contrib import auth
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

from users.forms import UserRegistrationForm, UserLoginForm


# Логин
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            # `authenticate` проверяет имя пользователя и пароль и возвращает `User` объект, если они правильные
            user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
            if user:
                auth.login(request, user)  # `login` устанавливает пользователя в текущую сессию
                return redirect('index')  # перенаправление на главную страницу после входа
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


# Регистрация
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # перенаправление на страницу входа после успешной регистрации
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})


# Выход
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
