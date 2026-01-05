import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoShopping(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10) # 10 second timer

    def test_add_backpack_to_cart(self):
        driver = self.driver
        wait = self.wait

        print("--- 1. Logging in ---")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        print("--- 2. Finding the Backpack ---")
        # We wait for the "Add to cart" button specifically for the Backpack
        # Note: I found this ID using Inspect Element!
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_btn.click()

        print("--- 3. Verifying Cart ---")
        # Look for the little red badge on the cart icon
        cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        
        # Get the text number from the badge (should be "1")
        items_count = cart_badge.text
        
        # The Final Proof
        self.assertEqual("1", items_count, "Cart count should be 1 after adding an item!")
        print("Success! Item added and verified. 🎒")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()