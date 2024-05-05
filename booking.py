# booking.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium import webdriver
import time
import datetime

from fullcode_one_way import email, phone


def is_valid_date(date_string):
    current_date = datetime.datetime.now().date()
    input_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return input_date >= current_date

def perform_booking():
    origin = "HYD"
    destination = "BLR"
    date = "24/04/2024"
    return_date = "23/05/2024"
    trip_type = "One Way"
    adults = 2
    childs = 1
    infants = 0

    # Chrome options to disable notifications
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")

    # Create a WebDriver instance with configured options
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(8)

    try:
        # Accessing the website
        driver.get("https://www.easemytrip.com/offers/no-convenience-fee.html")

        # Selecting trip type
        trip_type_elements = {
            "One Way": "/html[1]/body[1]/form[1]/div[4]/div[1]/div[3]/div[1]/ul[1]/li[1]",
            "Round Trip": "/html[1]/body[1]/form[1]/div[4]/div[1]/div[3]/div[1]/ul[1]/li[2]",
            "Multi City": "/html[1]/body[1]/form[1]/div[4]/div[1]/div[3]/div[1]/ul[1]/li[3]"
        }
        li_element = driver.find_element(By.XPATH, trip_type_elements[trip_type])
        li_element.click()
        time.sleep(2)

        # Maximizing window and handling final actions
        driver.maximize_window()
        time.sleep(3)

        # Enter origin
        driver.find_element(By.ID, "frmcity").click()
        origin_input = driver.find_element(By.ID, "a_FromSector_show")
        origin_input.clear()
        origin_input.send_keys(origin)
        time.sleep(3)
        driver.find_element(By.XPATH, f"//span[contains(text(),'{origin}')]").click()
        time.sleep(3)

        # Similarly for destination
        driver.find_element(By.ID, "tocity").click()
        destination_input = driver.find_element(By.ID, "a_Editbox13_show")
        destination_input.clear()
        destination_input.send_keys(destination)
        time.sleep(3)
        driver.find_element(By.XPATH, f"//span[contains(text(),'{destination}')]").click()
        time.sleep(3)

        # Enter departure date
        departure_date_input = driver.find_element(By.ID, "ddate")
        departure_date_input.click()
        time.sleep(3)

        try:
            # Check if the selected date is in the past
            selected_date = driver.find_element(By.ID, date)
            if selected_date.get_attribute("class") == "day past":
                print("Select the current date")
            else:
                selected_date.click()
                time.sleep(3)
        except NoSuchElementException:
            print("An error occurred: The selected date element is not found.")
        except ElementClickInterceptedException:
            print("Select the current date")

        # If round trip, enter return date
        if trip_type == "Round Trip":
            return_date_input = driver.find_element(By.ID, "rdate")
            return_date_input.click()
            time.sleep(2)
            driver.find_element(By.ID, return_date).click()
            time.sleep(2)

        # Adjust number of passengers
        traveller = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="myFunction4"]'))
        )
        traveller.click()
        time.sleep(3)  # Wait for any animations or subsequent UI changes

        # For adults
        while adults > 1:
            adult = driver.find_element(By.CSS_SELECTOR, ".add.plus_box1")
            adult.click()
            time.sleep(1)
            adults -= 1

        # For Childs
        while childs > 0:
            child = driver.find_element(By.CSS_SELECTOR, ".add.plus_boxChd")
            child.click()
            time.sleep(1)
            childs -= 1

        # Search flights
        click_search = driver.find_element(By.CSS_SELECTOR, ".srchBtnSe")
        click_search.click()
        time.sleep(4)

        # Maximizing window and handling final actions
        driver.maximize_window()
        time.sleep(3)

        # Find the button using XPath
        final_button_xpath = '//*[@id="ResultDiv"]/div/div/div[4]/div[2]/div[1]/div[2]/div[6]/button'

        try:
            # Wait for the button to be clickable
            final_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "btn.book-bt-n"))
            )

            # Click the button
            final_button.click()
            time.sleep(5)  # Wait for the page to load after clicking the button
        except TimeoutException:
            print("Timeout: The final button is not clickable.")
        except Exception as e:
            print(f"An error occurred while clicking the final button: {e}")

        # Scroll down after final action
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Additional operation
        yes = driver.find_element(By.XPATH, '//*[@id="divInsuranceTab"]/div[3]/div[1]/label')
        yes.click()
        time.sleep(2)

        # For email
        my = driver.find_element(By.XPATH, '//*[@id="txtEmailId"]')
        my.send_keys(email)
        time.sleep(2)

        # For continue booking
        book = driver.find_element(By.XPATH, '//*[@id="spnVerifyEmail"]')
        book.click()
        time.sleep(2)

        # Adult1 first name
        name1 = driver.find_element(By.CSS_SELECTOR, '#txtFNAdult0')
        name1.send_keys("Nayan")
        time.sleep(3)

        # Last name
        lname = driver.find_element(By.CSS_SELECTOR, '#txtLNAdult0')
        lname.send_keys("Asawa")
        time.sleep(3)

        # title
        title = driver.find_element(By.CSS_SELECTOR, '#titleAdult0')
        title.click()
        time.sleep(3)
        option = driver.find_element(By.XPATH, "//select[@id='titleAdult0']/option[@value='Mr']")
        option.click()
        time.sleep(3)

        # Adult 2 first name
        name2 = driver.find_element(By.CSS_SELECTOR, '#txtFNAdult1')
        name2.send_keys("Krishna")
        time.sleep(3)
        option = driver.find_element(By.XPATH, "//select[@id='titleAdult1']/option[@value='Mr']")
        option.click()
        time.sleep(3)

        # Adult last name
        Lname = driver.find_element(By.CSS_SELECTOR, '#txtLNAdult1')
        Lname.send_keys("Vyas")
        time.sleep(3)

        # For Child's First Name
        child_first_name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#txtFNChild0'))
        )
        child_first_name_input.send_keys("Madhav")
        time.sleep(3)

        # Select title for the child using Select class
        child_title_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'titleChild0'))
        )
        select = Select(child_title_dropdown)
        select.select_by_value("MSTR")  # Correct value for "Master"
        time.sleep(3)

        # Child lastName
        childLL = driver.find_element(By.CSS_SELECTOR, '#txtLNChild0')
        childLL.send_keys("Asawa")
        time.sleep(3)

        # phone number
        phone1 = driver.find_element(By.CSS_SELECTOR, '#txtCPhone')
        phone1.send_keys(phone)
        time.sleep(3)

        # submit
        submit = driver.find_element(By.CSS_SELECTOR, '#spnTransaction')
        submit.click()
        time.sleep(5)

        # trying skip
        skip1 = driver.find_element(By.ID, 'skipPop')
        skip1.click()
        time.sleep(8)

        # Skip popup
        popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "revw_rt_25"))
        )
        skip_button = popup.find_element(By.XPATH, ".//a[@class='edit_btn' and text()='Skip']")
        skip_button.click()
        time.sleep(2)

        # Another skip
        skip1 = driver.find_element(By.ID, 'skipPop')
        skip1.click()
        time.sleep(8)

    except Exception as e:
        print(f"An error occurred during booking: {e}")
    finally:
        driver.quit()
