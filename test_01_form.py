from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.maximize_window()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

waiter = WebDriverWait(driver, 40)
waiter.until(EC.visibility_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
waiter.until(EC.visibility_of_element_located((By.NAME, "last-name"))).send_keys("Петров")
waiter.until(EC.visibility_of_element_located((By.NAME, "address"))).send_keys("Ленина, 55-3")
waiter.until(EC.visibility_of_element_located((By.NAME, "zip-code"))).send_keys("")
waiter.until(EC.visibility_of_element_located((By.NAME, "city"))).send_keys("Москва")
waiter.until(EC.visibility_of_element_located((By.NAME, "country"))).send_keys("Россия")
waiter.until(EC.visibility_of_element_located((By.NAME, "e-mail"))).send_keys("test@skypro.com")
waiter.until(EC.visibility_of_element_located((By.NAME, "phone"))).send_keys("+7985899998787")
waiter.until(EC.visibility_of_element_located((By.NAME, "job-position"))).send_keys("QA")
waiter.until(EC.visibility_of_element_located((By.NAME, "company"))).send_keys("SkyPro")
button=driver.find_element(By.CSS_SELECTOR,"button.btn.btn-outline-primary.mt-3").click()
input("Press Enter to continue...")


def alert_danger(self):
     alert_danger = self._driver.find_element(By.CSS_SELECTOR, 'div.alert.py-2.alert-danger').value_of_css_property("background-color")
     return alert_danger

def alert_success(self):
    allert_success = self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
    for form in alert_success:
        return form.value_of_css_property("background-color")
    
assert alert_danger == "rgba(248, 215, 218, 1)"

assert alert_success == "rgba(209, 231, 221, 1)"


driver.quit()