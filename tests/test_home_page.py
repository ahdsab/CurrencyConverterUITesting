import unittest
from pages.home_page import HomePage
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
import time


class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.page_url = "http://localhost:3000"
        self.options = ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        return super().tearDown()
    
    def test_usd_to_ils(self):
        output = (self.home_page.open_home_page(self.page_url).
        set_amount(100).
        select_currency(self.home_page.get_from_selector(), "USD").
        select_currency(self.home_page.get_to_selector(), "ILS").
        click_convert_button().
        get_output())

        self.assertEqual(output, "380")



        
        






    

