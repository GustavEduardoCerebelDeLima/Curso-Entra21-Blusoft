from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Documentation/Python - https://selenium-python.readthedocs.io/
# Official Documentation - https://www.selenium.dev/


driver = webdriver.Firefox()
driver.get('https://www.google.com.br/')
driver.find_element(By.NAME, "q").send_keys('Senac' + Keys.ENTER)

