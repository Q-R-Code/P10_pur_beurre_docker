import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver import FirefoxOptions


class Test_functionnal_App_Account(StaticLiveServerTestCase):
    """Test correct register and connection form submission"""

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(firefox_options=opts)
        time.sleep(5)
        User.objects.create(username="user1", email="user1@user1.com", password="azerty").save()

    def test_register_then_connection_form_button(self):
        """test the path of a user from the creation of an account to the connection """

        self.driver.get(str(self.live_server_url) + '/compte/inscription/')
        time.sleep(5)
        username_input = self.driver.find_element_by_id('id_username')
        email_input = self.driver.find_element_by_id('id_email')
        password1_input = self.driver.find_element_by_id('id_password1')
        password2_input = self.driver.find_element_by_id('id_password2')
        submission_button = self.driver.find_element_by_id('register')
        time.sleep(5)
        username_input.send_keys('test')
        time.sleep(5)
        email_input.send_keys('test@gmail.com')
        time.sleep(5)
        password1_input.send_keys('123selenium')
        time.sleep(5)
        password2_input.send_keys('123selenium')
        time.sleep(5)
        submission_button.click()

        time.sleep(2)

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + '/compte/connection/login/', redirection_url)

        time.sleep(5)

        self.driver.get(str(self.live_server_url) + '/compte/connection/login')
        username_input = self.driver.find_element_by_id('id_username')
        password_input = self.driver.find_element_by_id('id_password')
        submission_button = self.driver.find_element_by_id('connection')
        time.sleep(5)
        username_input.send_keys('test')
        time.sleep(5)
        password_input.send_keys('123selenium')
        time.sleep(5)
        submission_button.click()

        time.sleep(2)

        redirection_url = self.driver.current_url
        self.assertEquals(self.live_server_url + "/", redirection_url)

        self.driver.quit()