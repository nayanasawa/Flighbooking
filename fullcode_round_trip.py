from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import datetime

def is_valid_date(date_string):
    current_date = datetime.datetime.now().date()
    input_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    return input_date >= current_date

origin = "HYD"
destination = "BLR"
date = "25/04/2024"
return_date = "05/05/2024"
trip_type = "Round Trip"
adults = 2
childs = 1
infants = 0
email = "nayan.asawa@nineleaps.com"
first1_N = "Nayan"
last1_N = "Asawa"
first2_N = "Krishna"
last2_N = "Vyas"
fchild1 = "Madhav"
lchild1 = "Asawa"
phone = "7793992929"
card1 = "371449635398431"
c1name = "NAYAN ASAWA"
cvv = "199"

# Check if the departure date is valid
if not is_valid_date(date):
    print("Departure date should not be the past date")
    exit()

# Check if return date is greater than or equal to departure date
departure_datetime = datetime.datetime.strptime(date, "%d/%m/%Y")
return_datetime = datetime.datetime.strptime(return_date, "%d/%m/%Y")
if return_datetime < departure_datetime:
    print("Return date must be greater than or equal to departure date")
    exit()

# Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

# Create a WebDriver instance with configured options
chrome_service = Service("/home/nineleaps/Downloads/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
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
    time.sleep(2)
    driver.find_element(By.XPATH, f"//span[contains(text(),'{origin}')]").click()
    time.sleep(2)

    # Similarly for destination
    driver.find_element(By.ID, "tocity").click()
    destination_input = driver.find_element(By.ID, "a_Editbox13_show")
    destination_input.clear()
    destination_input.send_keys(destination)
    time.sleep(2)
    driver.find_element(By.XPATH, f"//span[contains(text(),'{destination}')]").click()
    time.sleep(2)

    # Enter departure date
    departure_date_input = driver.find_element(By.ID, "ddate")
    departure_date_input.click()
    time.sleep(5)
    date_element = driver.find_element(By.ID, date)
    date_element.click()
    time.sleep(2)

    # If round trip, enter return date
    if trip_type == "Round Trip":
         return_date_input = driver.find_element(By.ID, "rdate")
         return_date_input.click()
         time.sleep(2)
         date_element = driver.find_element(By.ID, return_date)
         date_element.click()
         time.sleep(2)

    # Adjust number of passengers
    traveller = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="myFunction4"]'))
    )
    traveller.click()
    time.sleep(2)  # Wait for any animations or subsequent UI changes

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
    time.sleep(7)

    # book btn
    click_search = driver.find_element(By.ID, "BtnBookNow")
    click_search.click()
    time.sleep(3)

    # continue
    continuee = driver.find_element(By.XPATH, '//*[@id="DivMoreFareRT"]/div/div[3]/div/div/div[2]')
    continuee.click()
    time.sleep(5)

    # Maximizing window and handling final actions
    driver.maximize_window()
    time.sleep(3)

    # Find the button using CSS Selector and click it
    # final = driver.find_element(By.CSS_SELECTOR, '.btn.book-bt-n.ng-scope')
    # final.click()
    # time.sleep(5)

    # Scroll down after final action
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # clicking on yes
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
    name1.send_keys(first1_N)
    time.sleep(3)

    # Last name
    lname = driver.find_element(By.CSS_SELECTOR, '#txtLNAdult0')
    lname.send_keys(last1_N)
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
    name2.send_keys(first2_N)
    time.sleep(3)
    option = driver.find_element(By.XPATH, "//select[@id='titleAdult1']/option[@value='Mr']")
    option.click()
    time.sleep(3)

    # Adult last name
    Lname = driver.find_element(By.CSS_SELECTOR, '#txtLNAdult1')
    Lname.send_keys(last2_N)
    time.sleep(3)

    # child
    # child = driver.find_element(By.CSS_SELECTOR, '#txtFNChild0')
    # child.send_keys(fchild1)
    # time.sleep(3)
    # option = driver.find_element(By.XPATH, "//*[@id="titleChild0"]")
    # option.click()
    # time.sleep(5)

    # Access the webpage and perform necessary navigations

    # For Child's First Name
    child_first_name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#txtFNChild0'))
    )
    child_first_name_input.send_keys(fchild1)
    time.sleep(3)  # It's better to use WebDriverWait instead of sleep where possible

    # Select title for the child using Select class
    child_title_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'titleChild0'))
    )
    select = Select(child_title_dropdown)
    select.select_by_value("MSTR")  # Correct value for "Master"
    time.sleep(3)

    # CHild lastName
    childLL = driver.find_element(By.CSS_SELECTOR, '#txtLNChild0')
    childLL.send_keys(lchild1)
    time.sleep(3)

    # phoneNUmber
    phone1 = driver.find_element(By.CSS_SELECTOR, '#txtCPhone')
    phone1.send_keys(phone)
    time.sleep(4)

    # submit
    submit = driver.find_element(By.CSS_SELECTOR, '#spnTransaction')
    submit.click()
    time.sleep(4)

    # skip
    # Wait for the pop-up window to appear
    popup = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "revw_rt_25"))
    )

    # Find the "Skip" button within the pop-up
    skip_button = popup.find_element(By.XPATH, ".//a[@class='edit_btn' and text()='Skip']")

    # Click the "Skip" button
    skip_button.click()

    # Now, you can proceed with further actions after skipping the pop-up
    time.sleep(5)

    # continue booking click
    # booking = driver.find_element(By.XPATH, "//*[@id=\"DivContinueAncillary\"]/span")
    # bookig.click()
    # time.sleep(10)

    # trying skip
    skip1 = driver.find_element(By.ID, 'skipPop')
    skip1.click()
    time.sleep(4)

    # card
    # card = driver.find_element(By.XPATH, '//*[@id="card"]/div[1]/div[3]')
    # card.send_keys(card1)
    # time.sleep(15)

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
    time.sleep(4)

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
    time.sleep(4)

    # Wait for the button to be clickable
    # skip_button = WebDriverWait(driver, 10).until(
    #   EC.element_to_be_clickable((By.CLASS_NAME, "edit_btn"))
    # )

    # Scroll to the element
    # driver.execute_script("arguments[0].scrollIntoView(true);", skip_button)

    # Additional wait to handle any animations or JS events that might affect visibility
    # WebDriverWait(driver, 10).until(
    #   EC.visibility_of(skip_button)
    # )

    # Click the element
# skip_button.click()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the driver
    driver.quit()