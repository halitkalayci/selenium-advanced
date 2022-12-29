import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from constants import *

class TestAddToCart:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.vars = {}
  
    def teardown_method(self, method):
        self.driver.quit()

    def test_add_to_cart(self):
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR).click()
        self.driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR).send_keys(STANDARD_USER)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR).click()
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR).send_keys(USER_PASSWORD)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, INVENTORY_LIST)))
        #verilen ürün listesindeki tüm ürünleri sepete ekle..
        excelData = ["Sauce Labs Onesie","Sauce Labs Bike Light","123"]
        products = self.driver.find_elements(By.CSS_SELECTOR,INVENTORY_ITEMS)

        for i in range(len(products)):
            productName = products[i].find_element(By.CLASS_NAME,INVENTORY_ITEM_NAME).text
            # excelden gelen veri bu ürün ismini içeriyor mu?
            if excelData.__contains__(productName):
                addToCartBtn = products[i].find_element(By.CLASS_NAME,INVENTORY_BUTTON)
                addToCartBtn.click()

                
        self.driver.find_element(By.CLASS_NAME,CART_LINK).click()
        cartItems = self.driver.find_elements(By.CLASS_NAME,'cart_item')


        for i in range(len(cartItems)):
            productName = cartItems[i].find_element(By.CLASS_NAME,INVENTORY_ITEM_NAME).text
            if excelData.__contains__(productName) == False:
                assert False
        assert True