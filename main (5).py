# main.py
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

from booking import perform_booking
from fullcode_one_way import chrome_options
from payments import make_payment

# Create a WebDriver instance with configured options
chrome_service = Service("/home/nineleaps/Downloads/chromedriver-linux64/chromedriver")
driver = Chrome(service=chrome_service, options=chrome_options)
driver.implicitly_wait(8)

def main():
    try:
        # Perform flight booking
        perform_booking()

        # Perform payment
        make_payment()

        print("Booking and payment process completed successfully!")

    except Exception as e:
        print(f"An error occurred during the booking and payment process: {e}")

if __name__ == "__main__":
    main()
