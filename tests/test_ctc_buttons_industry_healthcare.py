import time

from pages.industry_healthcare_service_page import HealthCareServices
from pages.main_page import MainPage

def test_ctc_button_book_demo_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_HEALTHCARE_SERVICES)
    #time.sleep(2)
    hs = HealthCareServices(driver)
    #ma.scroll(3600)
    #ma.close_windows_popup()
    #ma.scroll(300)
    #time.sleep(2)
    hs.js_click(hs.BOOK_DEMO_BUTTON)
    assert hs.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_get_in_touch_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_HEALTHCARE_SERVICES)
    time.sleep(2)
    mp.scroll(3100)
    mp.close_windows_popup()
    time.sleep(2)
    hs = HealthCareServices(driver)
    hs.js_click(hs.GET_IN_TOUCH_BUTTON)
    time.sleep(2)
    assert "https://teldrip.com/contact" in driver.current_url, "Get in Touch button did not redirect to the correct URL"