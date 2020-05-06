from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from orders.models import Order

"""Форма регистрации"""
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Такой логин уже существует')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Такая почта уже используется')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)

                    # Авторизация и перенаправление на страницу входа
                    user.save()
                    messages.success(request, 'Регистрация прошла успешно, теперь вы можете авторизоваться')
                    return redirect('login')

                    # Авторизация сразу после регистрации
                    # auth.login(request, user)
                    # messages.success(request, 'Вы теперь авторизованы')
                    # return redirect('index')
        else:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

"""Форма авторизации"""
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Вы успешено авторизовались')
            return redirect('index')
        else:
            messages.error(request, 'Проверьте правильность введенных данных')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Вы успешно вышли из аккаунта')
    return render(request, 'pages/index.html')

def cart(request):
    user_orders = Order.objects.order_by('-price').filter(user_id=request.user.id)

    context = {
        'orders': user_orders
    }
    return render(request, 'accounts/cart.html', context)