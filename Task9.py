from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setup WebDriver (Replace 'chromedriver' with the path to your WebDriver if not in PATH)
driver = webdriver.Chrome()

try:
    # Step 1: Open the webpage
    driver.get("https://www.saucedemo.com/")

    # Step 2: Login with provided credentials
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for the page to load
    time.sleep(2)

    # Task 1: Get the title of the webpage
    page_title = driver.title
    print(f"Page Title: {page_title}")

    # Task 2: Get the current URL of the webpage
    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    # Task 3: Extract the entire contents of the webpage
    page_source = driver.page_source

    # Save the contents to a text file
    with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(page_source)
    print("Page content saved to 'Webpage_task_11.txt'")

finally:
    # Close the browser
    driver.quit()
