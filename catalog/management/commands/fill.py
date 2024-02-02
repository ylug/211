import json
# from django.core.management import BaseCommand
# from catalog.models import Category, Product
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         Category.objects.all().delete()
#         Product.objects.all().delete()
#
#         category_list = [
#             {'name': 'аудиотехника', 'description': 'колонки, наушники, проигрыватели и т.д'},
#             {'name': 'мобильные телефоны', 'description': 'телефоны и переферия'}
#         ]
#
#         category_for_create = []
#         for item in category_list:
#             category_for_create.append(Category(**item))
#
#         Category.objects.bulk_create(category_for_create)
#
#         products_list = [
#             {'name': 'Iphone 15 Pro Max', 'category': 2, 'price_for_one': 100_000},
#             {'name': 'Xiaomi Mi 11 lite', 'category': 2, 'price_for_one': 30_000},
#             {'name': 'Samsung buts lite', 'category': 1, 'price_for_one': 6_000},
#         ]
#
#         products_for_create = []
#         for item in products_list:
#             products_for_create.append(Product(**item))
#
#         Product.objects.bulk_create(products_for_create)


import json

from django.core.management import BaseCommand

from catalog.models import Product, Category
from config.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Заполнение базы данных фикстурами'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        with open(BASE_DIR / 'category.json', encoding='utf-8') as fp:
            category_data = json.load(fp)
            for item in category_data:
                Category.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"]
                )
        with open(BASE_DIR / 'product.json', encoding='utf-8') as fp:
            product_data = json.load(fp)
            for item in product_data:
                category_pk = item["fields"]["category"]
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk=item['pk'],
                    name=item["fields"]["name"],
                    description=item["fields"]["description"],
                    category=category,
                    price_for_one=item["fields"]["price_for_one"]
                )
