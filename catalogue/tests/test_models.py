from django.contrib.auth.models import User

from django.test import TestCase
from django.urls import reverse

from ..models import Product, Sub_saved




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

    def test_save_sub_db(self):
        self.client.force_login(self.user1)
        sub_id = self.product1.id
        old_sub = Sub_saved.objects.count()
        response = self.client.post(reverse('catalogue:save', args=[sub_id]))
        new_sub = Sub_saved.objects.count()
        self.assertEquals(new_sub, old_sub + 1)

    def test_delete_sub_db(self):
        self.client.force_login(self.user1)
        Sub_saved.objects.create(user_id=self.user1.id, sub_id=self.product1.id).save()
        sub_id = self.product1.id
        old_sub = Sub_saved.objects.count()
        response = self.client.post(reverse('catalogue:delete', args=[sub_id]))
        new_sub = Sub_saved.objects.count()
        self.assertEquals(new_sub, old_sub - 1)
