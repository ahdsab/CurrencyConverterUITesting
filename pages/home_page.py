from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.amount_input = (By.ID, "amountInput")
        self.from_select_input = (By.ID, "fromSelectInput")
        self.to_select_input = (By.ID, "toSelectInput")
        self.convert_button = (By.ID, "convertButton")
        self.output = (By.TAG_NAME, "p")
    
    def open_home_page(self, url: str):
        self.driver.get(url)
        return self
    
    def set_amount(self, amount: float):
        amount_element = self.driver.find_element(*self.amount_input)
        amount_element.clear()
        amount_element.send_keys(amount)
        return self

    def get_from_selector(self):
        return self.from_select_input
    
    def get_to_selector(self):
        return self.to_select_input

    def select_currency(self, selector, currency: str):
        select_input_element = self.driver.find_element(*selector)
        select = Select(select_input_element)
        select.select_by_visible_text(currency)
        return self

    def click_convert_button(self):
        convert_button_element = self.driver.find_element(*self.convert_button)
        convert_button_element.click()
        return self

    def get_output(self):
        output_element = self.driver.find_element(*self.output)
        return output_element.text
    

    

    




    