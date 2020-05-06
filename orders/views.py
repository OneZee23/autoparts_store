from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Order

def order(request):
    if request.method == 'POST':
        autopart_url = request.POST['autopart_url']
        autopart = request.POST['autopart']
        count = request.POST['count']
        price = request.POST['price']
        description = request.POST['description']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_ordered = Order.objects.all().filter(autopart_url = autopart_url, user_id = user_id)
            if has_ordered:
                messages.error(request, 'Вы уже добавляли данный товар в корзину')
                return redirect('/' + autopart_url)

        order = Order(autopart=autopart, autopart_url=autopart_url, count=count, description=description,
                      user_id=user_id, price=price)

        order.save()

        messages.success(request, 'Товар успешно добавлен в корзину')
        return redirect('/'+autopart_url)

