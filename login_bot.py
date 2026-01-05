from selenium import webdriver
from selenium.webdriver.common.by import By  # <--- New Import!
import time

# 1. Setup
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)  # Just to see the browser open

# 2. Find the Elements (The Locators you found)
# We store the actual HTML element inside a variable so we can use it later
user_box = driver.find_element(By.ID, "user-name")
pass_box = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "login-button")

print("Typing credentials...")
user_box.send_keys("standard_user")
pass_box.send_keys("secret_sauce")

print("Clicking login...")
time.sleep(1) # Waiting so you can see it type before clicking
login_btn.click()
if "inventory" in driver.current_url:
    print("Login Successful! We are in the store. 🛒")
else:
    print("Login Failed. ❌")
# 3. Wait and Close
time.sleep(5)
driver.quit()