# Generated by Django 4.2.7 on 2023-12-27 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='264797217328', max_length=15, verbose_name='Проверочный код'),
        ),
    ]