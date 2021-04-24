import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from seleniumlogin import force_login

from ..models import Product

class Test_Functionnal_App_Catalogue(StaticLiveServerTestCase):
    """Test search , save form submission"""

    def setUp(self):
        self.driver = webdriver.Firefox()
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

    def test_search_and_save_sub_button(self):
        """Force login , search a product, search a sub and save it.
        Then display the "my products" page to verify the presence of this one
        """
        force_login(self.user1, self.driver, self.live_server_url)
        self.driver.get(str(self.live_server_url) + '/search/?query=Produit1')
        search_button = self.driver.find_element_by_id('search-Produit1')
        search_button.click()

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + f"/{self.product1.id}/", redirection_url)

        time.sleep(2)

        save_button = self.driver.find_element_by_id('save-Produit2')
        save_button.click()

        time.sleep(2)

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/", redirection_url)

        time.sleep(2)

        self.driver.get(str(self.live_server_url) + '/mes-produits/')

        time.sleep(3)

        self.driver.quit()