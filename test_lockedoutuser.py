# Generated by Selenium IDE
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


class Testlockedoutuser():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(DRIVER_PATH)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_lockedoutuser(self):
    self.driver.get(BASE_URL) # refactor => magic string kaldırıldı..
    self.driver.maximize_window()
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR))) # magic string kaldırıldı
    self.driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR).click()
    self.driver.find_element(By.CSS_SELECTOR, USERNAME_INPUT_SELECTOR).send_keys(LOCKED_OUT_USER)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR)))
    self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT_SELECTOR).send_keys(USER_PASSWORD)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR)))
    self.driver.find_element(By.CSS_SELECTOR, LOGIN_BUTTON_SELECTOR).click()
    assert self.driver.find_element(By.CSS_SELECTOR, ERROR_ALERT_SELECTOR).text == LOCKED_OUT_USER_ERROR
  
