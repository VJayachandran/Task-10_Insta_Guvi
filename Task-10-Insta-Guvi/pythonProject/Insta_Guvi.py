from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

# Replace with the path to your WebDriver executable
driver_path = '/path/to/your/chromedriver'

# Replace with the Instagram profile URL you want to scrape
profile_url = 'https://www.instagram.com/Guviofficial/'

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Open the URL
    driver.get(profile_url)

    # Wait for the follower count to load (max wait time 10 seconds)
    follower_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[contains(text(), "followers")]/span' )))

    # Extract follower count
    follower_count = follower_count_element.get_attribute('title')

    # Wait for the following count to load (max wait time 10 seconds)
    following_count_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, './/*[contains(text(), "following")]/span')))

    # Extract following count
    following_count = following_count_element.get_attribute('title')

    # Print the results
    print(f'Followers: {follower_count}')
    print(f'Following: {following_count}')

finally:
    # Close the WebDriver
    driver.quit()