from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui

driver = webdriver.Edge()
driver.get('https://precos-de-produtos.netlify.app/')
sleep(3)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

botao_carregar_mais = driver.find_element(By.XPATH,"//button[@id='loadMoreButton']")
sleep(2)
botao_carregar_mais.click()
sleep(2)

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

driver.execute_script('window.scrollTo(0, 0);')
sleep(2)