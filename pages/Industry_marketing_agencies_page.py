from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MarketingAgencies(BasePage):
    CALENDER = (By.CSS_SELECTOR, ".calendly-popup-content")
    BOOK_DEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Book a Demo']")
    GET_IN_TOUCH_BUTTON = (By.XPATH, "//a[normalize-space()='Get in Touch']")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[normalize-space()='Subscribe']")
    SUBSCRIBE_EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    SUBSCRIBE_POPUP = (By.XPATH, "//div[@role='alert']")
    WINDOWS_POPUP = (By.XPATH, "//button[@class='close--popup']")


    def __init__(self, driver):
        super().__init__(driver)

    def click_subscribe(self):
        self.do_click(self.SUBSCRIBE_BUTTON)

    def is_subscribe_popup_displayed(self):
        return self.element_displayed(self.SUBSCRIBE_POPUP)

    def is_calender_displayed(self):
        return self.element_displayed(self.CALENDER)

    def close_windows_popup(self):
        if self.element_displayed(self.WINDOWS_POPUP):
            self.do_click(self.WINDOWS_POPUP)
        else:
            print("No popup to close")


