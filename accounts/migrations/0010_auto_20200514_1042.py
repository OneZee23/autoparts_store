# Generated by Django 3.0.5 on 2020-05-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200514_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_panel',
            name='photo',
            field=models.ImageField(blank=True, default='static/img/default.jpg', upload_to='users/', verbose_name='Аватар'),
        ),
    ]
