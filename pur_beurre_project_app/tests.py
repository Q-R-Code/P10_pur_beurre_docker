from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from pur_beurre_project.catalogue.models import *



class PagesTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def legal_notice_page(self):
        response = self.client.get(reverse('catalogue:legal-notice'))
        self.assertEqual(response.status_code, 200)


class ProductsTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="user", password="123456")
        Product.objects.create(
            name="Produit1",
            image_url="https://produit1-image-url.fr",
            categories=["Boissons", "Eaux", "breakfasts"],
            nutriscore_grade="b",
            image_nutriments="https://produit1-nutriments.fr",
            barcode="3274080005003",
            url="https://produit1-url.fr"
        )


    def test_search_page(self):
        query = "Produit1"
        response = self.client.get(reverse('catalogue:search'), {'query': query})
        print("TEST IS OK ")
        self.assertEqual(response.status_code, 200)

