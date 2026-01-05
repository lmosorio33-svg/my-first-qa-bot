import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_complete_purchase(self):
        driver = self.driver
        wait = self.wait
        
        # 1. Login
        print("1. Logging in...")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 2. Add to Cart
        print("2. Adding to cart...")
        add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_btn.click() 

        # 3. Go to Checkout
        print("3. Going to Checkout...")
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        
        # 4. Fill Shipping Info (FIXED SECTION)
        print("4. Filling Shipping info...")
        # FIX: We use 'wait' here because we just loaded a NEW page!
        wait.until(EC.url_contains("checkout-step-one"))
        # FIX: Use 'element_to_be_clickable' which checks if the box is Enabled/Ready
        first_name = wait.until(EC.element_to_be_clickable((By.ID, "first-name")))
        first_name.click()  # Click it first to wake it up (sometimes helps!)
        first_name.send_keys("Test")
        # The rest can be standard find_element because the page is now ready
        driver.find_element(By.ID, "last-name").send_keys("Bot")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()
        
        # 5. Finish
        print("5. Finishing Purchase...")
        wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click() 

        # 6. Verify
        print("6. Verifying Order Completion...")
        complete_header = driver.find_element(By.CLASS_NAME, "complete-header")
        actual_text = complete_header.text

        self.assertEqual("Thank you for your order!", actual_text, "Order completion message did not match!")
        print("Purchase completed successfully! 🎉")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()