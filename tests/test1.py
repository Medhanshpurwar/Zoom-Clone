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
        EC.presence_of_element_located((By.ID, "identifier-field"))  # Double-check the ID
    )
    email_field.clear()
    email_field.send_keys("medhanshpurwar@gmail.com")  # ✅ Use your email
    print("✅ Email entered successfully!")

    # ✅ Locate and click the continue button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cl-formButtonPrimary"))
    )
    continue_button.click()
    print("✅ Continue button clicked successfully!")

    # ⏳ Pause for manual login and meeting actions
    input("⏳ Please complete the login, start a new meeting, and press Enter to continue...")

    # ✅ Wait for a valid meeting URL to confirm meeting has started
    time.sleep(5)  # Add delay to allow page loading

    # ✅ Check if URL contains "/meeting/" after starting the meeting
    if "/meeting/" in driver.current_url:
        print(f"🎉✅ Test Case Passed: Meeting page loaded successfully at {driver.current_url}")
    else:
        print(f"❌ Test Case Failed: Current URL is {driver.current_url}, not a valid meeting page.")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # ⏸️ Delay to prevent auto browser close if user manually closes
    print("🔁 Waiting for 5 seconds to avoid session closure...")
    time.sleep(5)

    # ✅ Close browser only if still open
    try:
        driver.quit()
        print("🚪 Browser closed successfully.")
    except:
        print("✅ Browser was already closed. No action needed.")
