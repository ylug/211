# Generated by Django 4.2.7 on 2023-11-29 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='наименование')),
                ('description', models.CharField(max_length=150, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='наименование')),
                ('description', models.CharField(max_length=150, verbose_name='описание')),
                ('image', models.ImageField(upload_to='previews/', verbose_name='превью')),
                ('category', models.CharField(max_length=150, verbose_name='категория')),
                ('price_for_one', models.IntegerField(verbose_name='цена за штуку')),
                ('date_of_creation', models.DateTimeField(verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]