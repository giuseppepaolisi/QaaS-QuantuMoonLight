# Generated by Selenium IDE
"""
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

class TestDataset():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC211(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > label").click()
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
    self.driver.find_element(By.ID, "kFoldValue").click()
    self.driver.find_element(By.ID, "kFoldValue").send_keys("1")
    self.driver.find_element(By.ID, "submitForm").click()
  
  def test_tC212(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) > label").click()
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fa-rocket").click()
  
  def test_tC221(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\test.txt")
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.ID, "submitForm").click()
    assert self.driver.switch_to.alert.text == "Training set non inserito e/o non valido"
  
  def test_tC222(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.ID, "submitForm").click()
  
  def test_tC311(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > label").click()
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(7)").click()
    self.driver.find_element(By.ID, "nrRows").send_keys("0")
    self.driver.find_element(By.ID, "submitForm").click()
  
  def test_tC312(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) > label").click()
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.CSS_SELECTOR, "label:nth-child(7)").click()
    self.driver.find_element(By.ID, "nrRows").send_keys("11")
    self.driver.find_element(By.ID, "submitForm").click()
  
  def test_tC321(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > label").click()
    self.driver.find_element(By.ID, "nrColumns").click()
    self.driver.find_element(By.ID, "nrColumns").send_keys("0")
    self.driver.find_element(By.ID, "submitForm").click()
  
  def test_tC322(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.LINK_TEXT, "QUANTUM ML").click()
    self.driver.find_element(By.ID, "inputFakeBrowseFileTrain").click()
    self.driver.find_element(By.ID, "inputFileTrain").send_keys("C:\\fakepath\\Data_training.csv")
    self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > label").click()
    self.driver.find_element(By.LINK_TEXT, "Advanced Options").click()
    self.driver.find_element(By.ID, "nrColumns").click()
    self.driver.find_element(By.ID, "nrColumns").send_keys("15")
    self.driver.find_element(By.ID, "submitForm").click()
  """
