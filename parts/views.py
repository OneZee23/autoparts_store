from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from parts.choices import category_choices, automake_choices, price_choices, count_choices
from accounts.models import User_Panel
from .models import Autopart, Automake


class IndexView(ListView):
    """Главная страница"""
    model = Automake
    queryset = Automake.objects.all()
    template_name = "pages/index.html"


class AutopartsView(ListView):
    """Каталог товаров"""

    def get(self, request):
        listings = Autopart.objects.order_by('price').filter(draft=False)

        paginator = Paginator(listings, 4)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)

        context = {
            'autopart_list': paged_listings,
            'category_choices': category_choices,
            'automake_choices': automake_choices,
            'price_choices': price_choices,
            'count_choices': count_choices,
            'user_info': User_Panel.objects.all()
        }
        return render(request, 'pages/catalog.html', context)


class SearchView(ListView):
    """Выполненный поиск по каталогу товаров"""

    def get(self, request):
        queryset_list = Autopart.objects.order_by('price').filter(draft=False)

        # Поиск по названию
        if 'nametag' in request.GET:
            nametag = request.GET['nametag']
            if nametag:
                queryset_list = queryset_list.filter(title__icontains=nametag)

        # Категории
        if 'category' in request.GET:
            category = request.GET['category']
            if category:
                queryset_list = queryset_list.filter(category__name__iexact=category)

        # Категории
        if 'automake' in request.GET:
            automake = request.GET['automake']
            if automake:
                queryset_list = queryset_list.filter(automake__name__iexact=automake)

        # Категории
        if 'price' in request.GET:
            price = request.GET['price']
            if price:
                queryset_list = queryset_list.filter(price__lte=price)

        # Категории
        if 'count' in request.GET:
            count = request.GET['count']
            if count:
                queryset_list = queryset_list.filter(count__gte=count)

        paginator = Paginator(queryset_list, 2)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)

        context = {
            'autopart_list': paged_listings,
            'category_choices': category_choices,
            'automake_choices': automake_choices,
            'price_choices': price_choices,
            'count_choices': count_choices,
            'values': request.GET
        }
        return render(request, 'pages/search.html', context)


class AutopartsDetailView(DetailView):
    """Полное описание автозапчасти"""
    model = Autopart
    slug_field = "url"
    template_name = "pages/autopart_detail.html"
