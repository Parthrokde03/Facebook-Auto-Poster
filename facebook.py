from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()

# Use your Login Credentials
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "email"))
).send_keys("Your Email/Username")
driver.find_element(By.ID, "pass").send_keys("Your Password")
driver.find_element(By.NAME, "login").click()

time.sleep(5)
driver.get("https://www.facebook.com/home.php")
time.sleep(5)

try:
    create_post = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),\"What's on your mind\")]/ancestor::div[@role='button']"))
    )
    driver.execute_script("arguments[0].click();", create_post)
    print("Post box opened")
except Exception as e:
    print("Post box failed to open:", e)
    driver.quit()
    exit()

time.sleep(3)

try:
    textbox = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']//div[@role='textbox']"))
    )
    driver.execute_script("arguments[0].focus();", textbox)
    textbox.click()
    textbox.send_keys("Hi! there")
    print("Text typed")
except Exception as e:
    print("Failed to write post:", e)
    driver.quit()
    exit()

try:
    post_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post' and @role='button']"))
    )
    driver.execute_script("arguments[0].click();", post_btn)
    print("Post submitted")
except Exception as e:
    print("Post button click failed:", e)

time.sleep(5)
driver.quit()
