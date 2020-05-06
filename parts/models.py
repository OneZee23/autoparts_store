from django.db import models
from django.urls import reverse

class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Automake(models.Model):
    """Автопроизводители"""
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="automakes/", null=True)
    url = models.SlugField(max_length=160)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автопроизводитель"
        verbose_name_plural = "Автопроизводители"

class Autopart(models.Model):
    """Автозапчасти"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="autoparts/")
    automake = models.ManyToManyField(Automake, verbose_name="автопроизводитель", related_name="autopart_automake")
    count = models.PositiveSmallIntegerField("Количество", default=0)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    price = models.PositiveIntegerField("Цена", default=0, help_text="указать сумму в рублях")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("autopart_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Автозапчасть"
        verbose_name_plural = "Автозапчасти"