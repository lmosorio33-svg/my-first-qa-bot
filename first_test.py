from selenium import webdriver
import time

# 1. Start the Browser (This launches a robot-controlled Chrome window)
driver = webdriver.Chrome()

# 2. Go to the Website
print("Opening website...")
driver.get("https://www.python.org")

# 3. Get the Title of the page (The text on the browser tab)
page_title = driver.title
print("Page Title is: " + page_title)

# 4. Check if we are on the right page (The Test Logic)
if "Python" in page_title:
    print("Test Passed: We are on the Python website! ✅")
else:
    print("Test Failed: Wrong website. ❌")

# 5. Wait for 5 seconds so you can see it, then close
time.sleep(5)
driver.quit()