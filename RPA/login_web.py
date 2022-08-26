from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

# Documentation/Python - https://selenium-python.readthedocs.io/
# Official Documentation - https://www.selenium.dev/

driver = webdriver.Firefox()
driver.get('https://externo.proway.com.br/login-aluno')
driver.find_element('id', 'formLoginSubscriber_username').send_keys('cairo.andrade777@gmail.com' + Keys.TAB
                                                                    + '24092003' + Keys.ENTER)
# driver.find_element('id', 'formLoginSubscriber_password').send_keys('24092003' + Keys.ENTER)

sleep(3)
driver.find_element('xpath', '/html/body/div[1]/section/section/div[1]/div/div/div/ul/li[1]/ul/li/button').click()
sleep(2)
driver.find_element('xpath', '/html/body/div[1]/section/section/div[1]/div/div/div/ul/li[1]/ul/li/button').click()
sleep(2)
driver.find_element('xpath', '/html/body/div[1]/section/section/div[1]/div/div/div/ul/li[1]/ul/li/button').click()
sleep(2)
driver.find_element('xpath', '/html/body/div[1]/section/section/div[1]/div/div/div/ul/li[1]/ul/li/button').click()
driver.maximize_window()

