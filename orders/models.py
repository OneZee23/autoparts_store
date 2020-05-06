from django.db import models

class Order(models.Model):
    autopart = models.CharField(max_length=100)
    autopart_url = models.SlugField(max_length=160)
    price = models.PositiveIntegerField("Цена", default=0, help_text="указать сумму в рублях")
    count = models.PositiveSmallIntegerField("Количество", default=0)
    description = models.TextField("Описание", blank=True)
    user_id = models.IntegerField(blank=True)

