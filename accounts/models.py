from django.db import models

class User_Panel(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)
    email = models.CharField("e-mail", max_length=255)
    photo = models.ImageField("Аватар", upload_to='users/', blank=True, default='static/img/default.jpg')
    staff = models.BooleanField("Персонал", default=False)
    individual = models.BooleanField("Частное лицо", default=True)
    panel_id = models.IntegerField(blank=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

