import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # <--- The Timer
from selenium.webdriver.support import expected_conditions as EC # <--- The Conditions

class SauceDemoLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_valid_login(self):
        driver = self.driver
        # Create a "Waiter" that waits up to 10 seconds
        wait = WebDriverWait(driver, 10)

        # 1. Wait for username box to be visible, then type
        user_box = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        user_box.send_keys("standard_user")

        # 2. Wait for password box, then type
        pass_box = wait.until(EC.visibility_of_element_located((By.ID, "password")))
        pass_box.send_keys("secret_sauce")

        # 3. Wait for login button to be clickable, then click
        login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()

        # 4. Assert: Wait for the URL to change implies success
        # (This waits until the URL contains "inventory")
        wait.until(EC.url_contains("inventory"))
        print("Login successful and verified! 🚀")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()