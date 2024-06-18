from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from environment variables
username = os.getenv('ADMIN_USERNAME')
password = os.getenv('ADMIN_PASSWORD')

# Get proxy settings from environment variables
http_proxy = os.getenv('HTTP_PROXY')
https_proxy = os.getenv('HTTPS_PROXY')

def register_user(first_name, last_name, user_id, email):
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Set up the Chrome options to use the installed Chromium browser and Chromedriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    # Set proxy settings
    if http_proxy and https_proxy:
        proxy = f"{http_proxy};{https_proxy}"
        chrome_options.add_argument(f'--proxy-server={proxy}')

    # Initialize the WebDriver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # URL for the login page and upload page
    login_url = 'https://vu-vbl.sona-systems.com/'
    add_user_page_url = 'https://vu-vbl.sona-systems.com/admin_update_record.aspx?p_action=AF&p_type=E'

    try:
        # Open the login page
        logging.info('Opening login page...')
        driver.get(login_url)

        # Find and fill the username field
        logging.info('Filling in the username...')
        username_field = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_userid')
        username_field.send_keys(username)

        # Find and fill the password field
        logging.info('Filling in the password...')
        password_field = driver.find_element(By.ID, 'pw')
        password_field.send_keys(password)

        # Find and click the login button
        logging.info('Clicking the login button...')
        login_button = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_default_auth_button')
        login_button.click()

        # Wait for the login to complete and the page to load
        logging.info('Waiting for login to complete...')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_AdminNavigationBarUserControl_HomeLink')))

        # Navigate to the add user page
        logging.info('Navigating to the add user page...')
        driver.get(add_user_page_url)

        # Wait for the add user page to load
        logging.info('Waiting for the add user page to load...')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ctl00_ContentPlaceHolder1_txtFirstName')))

        # Fill the form
        logging.info('Filling in the user details...')
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtFirstName').send_keys(first_name)
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtLastName').send_keys(last_name)
        driver.find_element(By.ID, 'txtUserID').send_keys(user_id)
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_txtEmail').send_keys(email)

        # Check for duplicate user ID
        try:
            duplicate_message = driver.find_element(By.ID, 'showDuplicatetxtUserID')
            if duplicate_message.is_displayed():
                raise Exception('The User ID you have entered is already in use')
        except Exception as e:
            logging.error('Duplicate user ID error: ' + str(e))
            raise

        # Set reminder to No and email login info to Yes
        logging.info('Setting options...')
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_rdoReminderNo').click()
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_rdoEmailDetailsYes').click()

        # Submit the form
        logging.info('Submitting the form...')
        driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_Submit_Save_Changes').click()

        # Wait for the final confirmation to ensure the process is complete
        logging.info('Waiting for the final confirmation...')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'site-footer')))

        logging.info('User added successfully!')

    except Exception as e:
        logging.error(f'An error occurred: {e}')
        raise  # Re-raise the exception to ensure it gets displayed in Flask

    finally:
        # Close the WebDriver
        logging.info('Closing the WebDriver...')
        driver.quit()
