import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ✅ Path to chromedriver
driver_path = "C:\\Users\\medha\\Desktop\\Zoom\\ZOOM-CLONE\\tests\\chromedriver.exe"

# ✅ Launch Chrome browser
driver = webdriver.Chrome()

try:
    # ✅ Open the sign-in page
    driver.get("http://localhost:3000/sign-in")
    print("✅ Opened the sign-in page.")

    # ✅ Locate and enter email address
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifier-field"))  # Double-check ID
    )
    email_field.clear()
    email_field.send_keys("medhanshpurwar@gmail.com")
    print("✅ Email entered successfully!")

    # ✅ Locate and click the continue button
    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cl-formButtonPrimary"))
    )
    continue_button.click()
    print("✅ Continue button clicked successfully!")

    # ⏳ Wait for manual login and prompt
    input("⏳ Please complete the login, and press Enter to continue...")

    # ✅ Confirm if we are on the dashboard page
    if driver.current_url == "http://localhost:3000/":
        print("🎉✅ Test Case Passed: Logged into the dashboard successfully!")
    else:
        print(f"❌ Test Case Failed: Current URL is {driver.current_url}, not the dashboard.")
        driver.quit()
        exit()

    # ✅ Locate and click "Schedule Meeting" button to open pop-up
    schedule_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Schedule')]")  # Updated XPATH
        )
    )
    schedule_button.click()
    print("✅ Schedule Meeting button clicked, pop-up opened!")

    # ✅ Wait for pop-up to load
    time.sleep(2)

    # ✅ Enter meeting description
    description_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "description"))  # Change if name is different
    )
    description_field.clear()
    description_field.send_keys("Team sync-up for project.")
    print("✅ Description entered successfully!")

    # ✅ Select date and time (if required, update locators)
    date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "date"))  # Update 'name' if different
    )
    date_field.send_keys("2025-03-30")  # Format: YYYY-MM-DD
    print("✅ Date selected!")

    time_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "time"))  # Update 'name' if different
    )
    time_field.send_keys("10:30 AM")
    print("✅ Time selected!")

    # ✅ Click the final "Schedule Meeting" button
    confirm_schedule_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), 'Schedule Meeting')]")
        )
    )
    confirm_schedule_button.click()
    print("🎉✅ Meeting scheduled successfully!")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # ✅ Close the browser after test completion
    time.sleep(3)
    driver.quit()
    print("🚪 Browser closed successfully.")
