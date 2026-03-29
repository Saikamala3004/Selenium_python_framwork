from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )

    assert "Google" in driver.title

    driver.quit()