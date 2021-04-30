import requests
from django.core.management.base import BaseCommand

from catalogue.models import Product
from django.db import transaction, IntegrityError


class Command(BaseCommand):
    help = "Fill the database with products from API Openfoodfacts"
    def add_arguments(self, parser):
        parser.add_arguments('number', type=int, help='Indicates the number of products you wants to add.')

    def handle(self, *args, **options):
        number = kwargs['number']
        url = f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=unique_scans_n&?sort_by=popularity&page_size={number}&json=true"
        req = requests.get(url)
        data = req.json()
        prod = data["products"]
        number_prod = 0
        for x in prod:
            try:
                name = x["product_name"]
                image_url = x["image_url"]
                categories_tag = x["categories_hierarchy"]
                categories = []
                for cat in categories_tag:
                    categories.append(cat[3:])
                nutriscore_grade = x["nutriscore_grade"]
                image_nutrition = x["image_nutrition_url"]
                barcode = x["code"]
                url = x["url"]
                product = Product(name=name, categories=categories, image_url=image_url,
                                nutriscore_grade=nutriscore_grade,
                                image_nutriments=image_nutrition, barcode=barcode, url=url)
                if not Product.objects.filter(name=product.name):
                    product.save()
                    number_prod += 1
                    if number_prod %10 == 0:
                        self.stdout.write(f'Loading: "{number_prod}" products are saved!')

            except:
                self.stdout.write(f'Exception : {name} not saved ...')
        self.stdout.write(f'Fill_db : {number_prod} products are saved!')
