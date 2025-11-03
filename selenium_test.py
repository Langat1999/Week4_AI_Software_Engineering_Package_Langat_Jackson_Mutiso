# Task 2: Automated Testing with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login(driver, username, password, expected_success):
    driver.get('https://the-internet.herokuapp.com/login')
    time.sleep(2)  # Wait for page load

    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    time.sleep(2)  # Wait for response

    if expected_success:
        success_msg = driver.find_element(By.ID, 'flash').text
        if 'You logged into a secure area!' in success_msg:
            print("Login successful for valid credentials.")
            return True
        else:
            print("Login failed unexpectedly for valid credentials.")
            return False
    else:
        error_msg = driver.find_element(By.ID, 'flash').text
        if 'Your username is invalid!' in error_msg or 'Your password is invalid!' in error_msg:
            print("Login correctly failed for invalid credentials.")
            return True
        else:
            print("Login unexpectedly succeeded for invalid credentials.")
            return False

driver = webdriver.Chrome()

# Test valid credentials
valid_success = test_login(driver, 'tomsmith', 'SuperSecretPassword!', True)

# Test invalid credentials
invalid_success = test_login(driver, 'invaliduser', 'wrongpass', False)

# Overall results
total_tests = 2
passed_tests = (1 if valid_success else 0) + (1 if invalid_success else 0)
print(f"Tests passed: {passed_tests}/{total_tests}")

# Save screenshot
driver.save_screenshot('login_test_result.png')
print("Screenshot saved as login_test_result.png")

driver.quit()

"""
Summary (150 words):
Automated testing with Selenium, enhanced by AI plugins like Testim.io, significantly improves test coverage compared to manual testing. Manual testing is time-consuming, error-prone, and limited by human fatigue, often missing edge cases or requiring repetitive execution. AI-driven tools automate script generation, detect UI changes, and suggest test scenarios, allowing for broader coverage including cross-browser and device variations. For instance, in this login test, AI can generate scripts for multiple credential combinations, capture failures accurately, and integrate with CI/CD for continuous testing. This reduces development time, increases reliability, and enables regression testing at scale. While manual testing offers intuitive insights, AI ensures consistency and depth, making it ideal for complex applications. Overall, AI transforms testing from a bottleneck to an efficient, intelligent process, enhancing software quality and developer productivity.
"""
