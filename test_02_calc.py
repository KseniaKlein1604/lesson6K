from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
waiter = WebDriverWait(driver, 50)
driver.maximize_window()

delay = driver.find_element(By.CSS_SELECTOR, '#delay')
delay.clear()
delay.send_keys('45')
button = driver.find_element(By.XPATH, "//*[contains(text(),'7')]").click()
button=driver.find_element(By.XPATH, "//*[contains(text(),'+')]").click()
button = driver.find_element(By.XPATH, "//*[contains(text(),'8')]").click()
button=driver.find_element(By.XPATH, "//*[contains(text(),'=')]").click()

equals_button = WebDriverWait(driver, 46).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))
)

def screen(self):
    screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
    WebDriverWait(self._driver, 50).until(
         EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
         )
assert result, "Результат равен 15"
driver.quit()
