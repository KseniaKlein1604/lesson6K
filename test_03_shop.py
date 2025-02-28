from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

waiter = WebDriverWait(driver, 40)
button_user = driver.find_element(By.ID, 'user-name').send_keys("standard_user")
button_password = driver.find_element(By.ID, 'password').send_keys("secret_sauce")
button_login = driver.find_element(By.ID, 'login-button').click()

button_add_backpack = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
button_add_shirt = driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
button_add_sauce_labs = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

waiter = WebDriverWait(driver, 40)
button_cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
button_checkout = driver.find_element(By.ID, 'checkout').click()


button_first_name = driver.find_element(By.ID, 'first-name').send_keys("Ksenia")
button_last_name = driver.find_element(By.ID, 'last-name').send_keys("Rayevskaya")
button_zip_code = driver.find_element(By.ID, 'postal-code').send_keys("12345678")

button_continue = driver.find_element(By.ID, 'continue').click()

total=driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
print(f'Total: {total}')
clean_total = total.replace('Total: ', '').strip()
assert clean_total == '$58.29'
input("Press Enter to continue...")
driver.quit()



