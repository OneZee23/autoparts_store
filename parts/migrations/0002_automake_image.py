# Generated by Django 3.0.5 on 2020-05-01 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='automake',
            name='image',
            field=models.ImageField(null=True, upload_to='automakes/', verbose_name='Изображение'),
        ),
    ]
