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

class TestRegistrazione():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC111(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC112(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123cfsdil.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC113(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("123456")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC114(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADeCurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "confirmPassword").send_keys("123456")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC115(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Password123")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC116(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Password123")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC117(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADecurtis123@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("Password123")
    self.driver.find_element(By.ID, "confirmPassword").send_keys("Password123")
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92<316")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
  def test_tC118(self):
    self.driver.get("http://0.0.0.0:5000/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.CSS_SELECTOR, ".user").click()
    self.driver.find_element(By.LINK_TEXT, "Register Here").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("ADeCurtis123@gmail.com")
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("Password123 ")
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("Antonio de Curtis")
    self.driver.find_element(By.ID, "nome").send_keys("Antonio")
    self.driver.find_element(By.ID, "cognome").send_keys("de Curtis")
    self.driver.find_element(By.ID, "token").send_keys("0e906980a743e9313c848becb8810b2667535e188365e8db829e1c206421d1ec02360127de06b13013782ca87efc3b7487853aba99061df220b825adee92e316 ")
    self.driver.find_element(By.CSS_SELECTOR, ".fourth").click()
  
