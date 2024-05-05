# payment.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time

def make_payment():
    card1 = "371449635398431"
    c1name = "NAYAN ASAWA"
    cvv = "199"

    # Chrome options to disable notifications
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    # Create a WebDriver instance with configured options
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(8)

    try:
        # Accessing the website
        driver.get("https://www.easemytrip.com/offers/no-convenience-fee.html")

        # Your payment related code here
        print("Making payment...")
        # Example function for making payment
        # ...

        # Wait until the input for the card number is visible and interactable
        card_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "CC"))
        )
        card_input.send_keys(card1)
        time.sleep(4)

        # card name
        cname = driver.find_element(By.ID, "CCN")
        cname.send_keys(c1name)
        time.sleep(4)

        # for cvv
        cvvv = driver.find_element(By.ID, "CCCVV")
        cvvv.send_keys(cvv)
        time.sleep(3)

        # for month
        dropdown = driver.find_element(By.ID, "CCMM")
        # Create a Select object
        select_object = Select(dropdown)
        # Select the option for March
        select_object.select_by_value("03")  # The value "03" corresponds to March
        # Optional: Wait for some time to observe the changes
        time.sleep(4)

        # for year
        # Locate the dropdown element
        dropdown = driver.find_element(By.ID, "CCYYYY")
        # Create a Select object
        select_object = Select(dropdown)
        # Select the option for the year 2028
        select_object.select_by_value("2028")
        # Optional: Wait for some time to observe the changes
        time.sleep(4)

        # make payment
        payment = driver.find_element(By.XPATH, '//*[@id="card"]/div[12]')
        # Click on the "Make Payment" element
        payment.click()
        # Optional: Wait for some time to observe the changes
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred during payment: {e}")
    finally:
        driver.quit()
