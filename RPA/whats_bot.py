from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

# Documentation/Python - https://selenium-python.readthedocs.io/
# Official Documentation - https://www.selenium.dev/

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')
sleep(15)
driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
sleep(2)
driver.find_element('xpath', '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys('Hen' + Keys.ENTER)
sleep(2)
# driver.find_element('xpath', '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[11]/div/div/div[2]/div[1]/div[1]/span').click()
# sleep(2)

# driver.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').click()
# sleep(2)

msg = 'oi, bom dia!'
for i in msg:
    driver.find_element('xpath',
                        '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(f'{i}')

sleep(2)
driver.find_element('xpath', '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()

driver.maximize_window()
