import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse
from selenium import webdriver
from seleniumlogin import force_login

from ..models import Product, Search_history


class TestViews(TestCase):
    """Test some views"""

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/index.html')

    def test_legal_view(self):
        response = self.client.get(reverse('catalogue:legal-notice'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/legal-notice.html')


class TestProducts(TestCase):
    """
    Test a few views and test searching, saving and deleting.
    """

    def setUp(self):
        Product.objects.create(
            name="Produit1",
            image_url="https://produit1-image-url.fr",
            categories=['Boissons', 'Eaux', 'breakfasts'],
            nutriscore_grade="b",
            image_nutriments="https://produit1-nutriments.fr",
            barcode="3274080011111",
            url="https://produit1-url.fr"
        ).save()
        Product.objects.create(
            name="Produit2",
            image_url="https://produit2-image-url.fr",
            categories="[Boissons, Eaux, breakfasts]",
            nutriscore_grade="b",
            image_nutriments="https://produit2-nutriments.fr",
            barcode="3274080022222",
            url="https://produit2-url.fr"
        ).save()
        User.objects.create(username="user1", email="user1@user1.com", password="azerty").save()
        self.user1 = User.objects.get(username="user1")
        self.product1 = Product.objects.get(name="Produit1")
        self.product2 = Product.objects.get(name="Produit2")

    def test_search_view_none(self):
        response = self.client.get(reverse('catalogue:search'))
        self.assertEquals(response.status_code, 302, "Vous n'avez rien saisi")
        self.assertTemplateUsed(redirect('index.html'))

    def test_search_view_good(self):
        response = self.client.get(reverse('catalogue:search'), {'query': 'Product1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/search.html')

    def test_search_view_bad(self):
        response = self.client.get(reverse('catalogue:search'), {'query': 'Badname'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/search.html')

    def test_detail_view(self):
        product_id = self.product1.id
        response = self.client.get(reverse('catalogue:detail', args=[product_id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalogue/detail.html')


class Test_Functionnal_App_Catalogue(StaticLiveServerTestCase):
    """Test search , save form submission"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        time.sleep(5)
        Product.objects.create(
            name="Produit1",
            image_url="https://produit1-image-url.fr",
            categories=['Boissons', 'Eaux', 'breakfasts'],
            nutriscore_grade="b",
            image_nutriments="https://produit1-nutriments.fr",
            barcode="3274080011111",
            url="https://produit1-url.fr"
        ).save()
        Product.objects.create(
            name="Produit2",
            image_url="https://produit2-image-url.fr",
            categories=['Boissons', 'Eaux', 'breakfasts'],
            nutriscore_grade="b",
            image_nutriments="https://produit2-nutriments.fr",
            barcode="3274080022222",
            url="https://produit2-url.fr"
        ).save()
        User.objects.create(
            username="user1", email="user1@user1.com", password="azerty"
        ).save()

        self.user1 = User.objects.get(username="user1")
        self.product1 = Product.objects.get(name="Produit1")
        self.product2 = Product.objects.get(name="Produit2")

    def test_query_my_page(self):
        """Force login , search a product 11 times and checks that there are only 10 searches for the user.
        Then test "clean history" and checks that there are nothing in the tables.

        """
        force_login(self.user1, self.driver, self.live_server_url)
        time.sleep(5)
        for x in range(11):
            self.driver.get(str(self.live_server_url) + f'/search/?query=Produit{x}')
            time.sleep(1)
        query = Search_history.objects.filter(user_id=self.user1.id)
        self.assertEquals(query.count(), 10)

        query2 = Search_history.objects.filter(user_id=self.user1.id, query__icontains='Produit0')
        self.assertEquals(query2.count(), 0)

        self.driver.get(str(self.live_server_url) + '/mon-compte/')
        clean_button = self.driver.find_element_by_id('clean_history')
        clean_button.click()
        time.sleep(1)
        query3 = Search_history.objects.filter(user_id=self.user1.id)
        self.assertEquals(query3.count(), 0)
        self.driver.quit()
