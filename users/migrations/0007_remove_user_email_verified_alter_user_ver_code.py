# Generated by Django 5.0.1 on 2024-02-02 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_ver_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_verified',
        ),
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='959215320807', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
