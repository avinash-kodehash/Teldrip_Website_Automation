import time

from pages.industry_telecom_page import Telecom
from pages.main_page import MainPage

def test_ctc_button_book_demo_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_TELECOM)
    #time.sleep(2)
    t = Telecom(driver)
    #ma.scroll(3600)
    #ma.close_windows_popup()
    #ma.scroll(300)
    #time.sleep(2)
    t.js_click(t.BOOK_DEMO_BUTTON)
    assert t.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_get_in_touch_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_TELECOM)
    time.sleep(2)
    mp.scroll(3100)
    mp.close_windows_popup()
    time.sleep(2)
    t = Telecom(driver)
    t.js_click(t.GET_IN_TOUCH_BUTTON)
    time.sleep(2)
    assert "https://teldrip.com/contact" in driver.current_url, "Get in Touch button did not redirect to the correct URL"