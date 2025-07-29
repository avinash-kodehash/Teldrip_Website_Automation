from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class VirtualNumber(BasePage):

    CALENDER = (By.CSS_SELECTOR,".calendly-popup-content")
    SCHEDULE_DEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Schedule Demo']")
    BOOK_DEMO_BUTTON = (By.XPATH, "//button[normalize-space()='Book a Demo']")
    SUBSCRIBE_BUTTON = (By.XPATH, "//button[normalize-space()='Subscribe']")
    SUBSCRIBE_EMAIL = (By.XPATH, "//input[@placeholder='Enter your email']")
    WINDOWS_POPUP = (By.XPATH, "//button[@class='close--popup']")
    SUBSCRIBE_POPUP = (By.XPATH, "//div[@role='alert']")
    SEE_HOW_CONNECT_WORKS = (By.XPATH, "//a[normalize-space()='See How Teldrip Connect Works']")

    def __init__(self, driver):
        super().__init__(driver)

    def is_calender_displayed(self):
        return self.element_displayed(self.CALENDER)


    def click_schedule_demo(self):
        self.do_click(self.SCHEDULE_DEMO_BUTTON)

    def close_windows_popup(self):
        if self.element_displayed(self.WINDOWS_POPUP):
            self.do_click(self.WINDOWS_POPUP)
        else:
            print("No popup to close")

    def click_subscribe(self):
        self.do_click(self.SUBSCRIBE_BUTTON)

    def is_subscribe_popup_displayed(self):
        return self.element_displayed(self.SUBSCRIBE_POPUP)