# Generated by Django 3.0.5 on 2020-05-14 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200514_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_panel',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='user_panel',
            name='username',
        ),
        migrations.AddField(
            model_name='user_panel',
            name='individual',
            field=models.BooleanField(default=False, verbose_name='Частное лицо'),
        ),
        migrations.AddField(
            model_name='user_panel',
            name='user_id',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
