# Generated by Django 5.0.1 on 2024-02-02 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='259353915265', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
