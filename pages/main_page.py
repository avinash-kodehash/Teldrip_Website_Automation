from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class MainPage(BasePage):
    ALL_BUTTONS = (By.XPATH,"//button")
    CALENDER = (By.CSS_SELECTOR,".calendly-popup-content")
    REQUEST_DEMO_BUTTON = (By.XPATH,"//button[normalize-space()='Request Demo']")
    SEE_PRICING_BUTTON = (By.XPATH,"//a[normalize-space()='See Pricing']")
    SCHEDULE_DEMO_BUTTON = (By.XPATH,"//button[normalize-space()='Schedule Demo']")
    WINDOWS_POPUP = (By.XPATH,"//button[@class='close--popup']")
    SUBSCRIBE_POPUP = (By.XPATH,"//div[@role='alert']")
    #Contact info
    FIRST_NAME = (By.ID,"first_name")
    LAST_NAME = (By.ID,"last_name")
    EMAIL = (By.ID,"emailid")
    PHONE = (By.XPATH,"//input[@placeholder='Enter your Phone number']")
    MESSAGE = (By.XPATH,"//textarea[@placeholder='Message']")
    SUBMIT_BUTTON = (By.XPATH,"//button[normalize-space()='Submit']")
    CONTACT_CONFIRM_MSG = (By.XPATH,"//div[@role='alert']")
    SUBSCRIBE_BUTTON = (By.XPATH,"//button[normalize-space()='Subscribe']")
    SUBSCRIBE_EMAIL = (By.XPATH,"//input[@placeholder='Enter your email']")
    #Products
    PRODUCTS_LINK = (By.XPATH,"(//a[normalize-space()='Products'])[1]")
    INDUSTRIES_LINK = (By.XPATH,"(//a[normalize-space()='Industries'])[1]")
    INSIGHTS = (By.XPATH,"//div[@class='insight']/a[@href='/insights']")
    CONNECT = (By.XPATH,"//div[@class='insight']/a[@href='/connect']")
    INSIGHT_CALL_TRACKING = (By.XPATH,"//div[@class='articleloop']/a[@href='/call-tracking-software']")
    INSIGHT_CALL_REPORTING = (By.XPATH,"//div[@class='articleloop']/a[@href='/call-reporting']")
    INSIGHT_PAYOUT_MANAGEMENT = (By.XPATH,"//div[@class='articleloop']/a[@href='/payout-management']")
    INSIGHT_CALL_ROUTING = (By.XPATH,"//div[@class='articleloop']/a[@href='/call-routing-software']")
    INSIGHTS_PAY_PER_CALL = (By.XPATH,"//div[@class='articleloop']/a[@href='/pay-per-call']")
    INSIGHTS_REAL_TIME_BIDDING = (By.XPATH,"//div[@class='articleloop']/a[@href='/real-time-bidding']")
    CONNECT_COMMUNICATION_MANAGEMENT = (By.XPATH,"//h5[normalize-space()='Communication Management']")
    CONNECT_CALL_MANAGEMENT = (By.XPATH,"//h5[normalize-space()='Call Management']")
    CONNECT_AUTODIALER = (By.XPATH,"//h5[normalize-space()='Autodialer']")
    CONNECT_CAMPAIGN = (By.XPATH,"//h5[normalize-space()='Campaigns']")
    CONNECT_VIRTUAL_PHONE_NUMBER = (By.XPATH,"//h5[normalize-space()='Virtual Phone Number']")
    CONNECT_WORKFORCE_MANAGEMENT = (By.XPATH,"//h5[normalize-space()='Workforce Management']")
    INDUSTRY_MARKETING_AGENCY = (By.XPATH,"//div[@class='articleloop']/a[@href='/industry/marketing-agencies']")
    INDUSTRY_AUTOMOTIVE = (By.XPATH,"//div[@class='articleloop']/a[@href='/industry/automotive']")
    INDUSTRY_LEGAL_SERVICES = (By.XPATH,"//a[@href='/industry/legal-services']")
    INDUSTRY_FINANCIAL_SERVICES = (By.XPATH,"//a[@href='/industry/financial-services']")
    INDUSTRY_HEALTHCARE_SERVICES = (By.XPATH,"//a[@href='/industry/healthcare-services']")
    INDUSTRY_TELECOM = (By.XPATH,"//a[@href='/industry/telecom']")
    INDUSTRY_SALES = (By.XPATH,"//a[@href='/industry/sales']")
    INDUSTRY_TRAVEL_HOSPITALITY = (By.XPATH,"//a[@href='/industry/travel-hospitality']")

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