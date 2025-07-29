from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InsightPage(BasePage):

    CALENDER = (By.CSS_SELECTOR, ".calendly-popup-content")
    REQUEST_DEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Request Demo']")
    SEE_PRICING_BUTTON = (By.XPATH, "//a[normalize-space()='See Pricing']")
    SCHEDULE_DEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Schedule Demo']")
    WINDOWS_POPUP = (By.XPATH, "//button[@class='close--popup']")
    SUBSCRIBE_POPUP = (By.XPATH, "//div[@role='alert']")
    # Contact info
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    EMAIL = (By.ID, "emailid")
    PHONE = (By.XPATH, "//input[@placeholder='Enter your Phone number']")
    MESSAGE = (By.XPATH, "//textarea[@placeholder='Message']")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Submit']")
    CONTACT_CONFIRM_MSG = (By.XPATH, "//div[@role='alert']")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[normalize-space()='Subscribe']")
    SUBSCRIBE_EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_calender_displayed(self):
        return self.element_displayed(self.CALENDER)

    def fill_contact_info(self, first_name, last_name, email, phone, message):
        self.write(self.FIRST_NAME, first_name)
        self.write(self.LAST_NAME, last_name)
        self.write(self.EMAIL, email)
        self.write(self.PHONE, phone)
        self.write(self.MESSAGE, message)

    def click_request_demo(self):
        self.do_click(self.REQUEST_DEMO_BUTTON)

    def click_see_pricing(self):
        self.do_click(self.SEE_PRICING_BUTTON)

    def click_schedule_demo(self):
        self.do_click(self.SCHEDULE_DEMO_BUTTON)

    def click_submit(self):
        self.do_click(self.SUBMIT_BUTTON)

    def is_contact_confirmation_msg_displayed(self):
        return self.element_displayed(self.CONTACT_CONFIRM_MSG)

    def close_windows_popup(self):
        if self.element_displayed(self.WINDOWS_POPUP):
            self.do_click(self.WINDOWS_POPUP)
        else:
            print("No popup to close")

    def click_subscribe(self):
        self.do_click(self.SUBSCRIBE_BUTTON)

    def is_subscribe_popup_displayed(self):
        return self.element_displayed(self.SUBSCRIBE_POPUP)