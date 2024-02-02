from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='previews/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price_for_one = models.IntegerField(verbose_name='цена за штуку', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    publication = models.BooleanField(default=False, verbose_name="статус публикакции")

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    def price(self):
        return f'{self.price_for_one} руб.'

    def info(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'
        permissions = [
            (
                'set_publication',
                'Can change status publication'
            ),
            (
                'set_category',
                'Can change category'
            ),
            (
                'set_description',
                'Can change description'
            )
        ]


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, unique=True, verbose_name='Ссылка', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE)
    image = models.ImageField(default='479679246.jpg', upload_to='blogs/', verbose_name='Изображение', **NULLABLE)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', **NULLABLE)
    date_modified = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано', **NULLABLE)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров', **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.slug}'

    class Meta:
        verbose_name = 'статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'статьи'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    title = models.CharField(max_length=100, verbose_name='название версии')
    number = models.IntegerField(verbose_name='номер версии', **NULLABLE)
    current_version = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'