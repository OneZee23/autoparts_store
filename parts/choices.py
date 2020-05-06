from .models import Automake, Category

category_choices = dict()
for category in Category.objects.all():
    category_choices.setdefault(category.name, category.name)

automake_choices = dict()
for automake in Automake.objects.all():
    automake_choices.setdefault(automake.name, automake.name)

price_choices = {
    '10': 10,
    '100': 100,
    '500': 500,
    '1000': 1000,
    '5000': 5000,
    '10000': 10000
}

count_choices = {
    '1': 1,
    '5': 5,
    '10': 10,
    '20': 20,
    '50': 50,
    '100': 100
}