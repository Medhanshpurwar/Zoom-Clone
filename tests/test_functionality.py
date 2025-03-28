import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ Launch Chrome browser
driver = webdriver.Chrome()

try:
    # ✅ Open the sign-in page
    driver.get("http://localhost:3000/sign-in")
    print("✅ Opened the sign-in page.")

    # ✅ Locate and enter email address
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifier-field"))
    )
    email_field.send_keys("medhanshpurwar@gmail.com")
    print("✅ Email entered successfully!")

    # ✅ Locate and click the continue button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cl-formButtonPrimary"))
    )
    continue_button.click()
    print("✅ Continue button clicked successfully!")

    # ⏱️ Add a delay of 2-4 seconds after clicking continue
    time.sleep(3)  # You can change 3 to any value between 2-4 seconds

    # ✅ Wait for the URL to change to the dashboard
    WebDriverWait(driver, 10).until(EC.url_to_be("http://localhost:3000/"))

    # ✅ Check if we are on the correct URL
    if driver.current_url == "http://localhost:3000/":
        print("🎉✅ Test Case Passed: Successfully logged into the dashboard!")
    else:
        print(f"❌ Test Case Failed: Current URL is {driver.current_url}, not the dashboard.")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # ✅ Close the browser
    driver.quit()
    
