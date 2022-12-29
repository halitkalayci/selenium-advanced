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
import openpyxl

class TestProductsOrderByPrice:
    def setup_method(self, method):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()

    def test_products_order(self):
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR).send_keys(STANDARD_USER)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR).send_keys(USER_PASSWORD)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR)))
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR).click()
        # burdan sonrası değişmeli..
        self.driver.find_element(By.XPATH,LOW_TO_HIGH_OPTION).click()
        # ürünler sıralandı.. 
        # doğrulama!!
        products = self.driver.find_elements(By.CSS_SELECTOR,INVENTORY_ITEMS)
        # bu listeyi baştan sona gez, eğer o anki ürün fiyatı bi önceki ürün fiyatından düşükse
        # test hatalıdır..
        # 10₺ 20₺ 30₺ 40₺
        # 10₺ 20₺ 9₺ 20₺
        lastPrice = -1
        testCase=True
        for i in range(len(products)):
            # ürünün fiyatı
            price = products[i].find_element(By.CLASS_NAME,PRICE_CLASS).text
            # $ işaretini kaldır ve floata çevir
            actualPrice = float(price.split('$')[1])  # 7.99
            # "123,456,789"  => split(',') => ["123","456","789"]
            # $7.99 => split('$') => ['','7.99'] -> seperator
            if actualPrice < lastPrice:
                testCase=False
            else:
                lastPrice = actualPrice
        assert testCase == True

