import time
from pages.main_page import MainPage
from pages.industry_automotive_page import Automotive

def test_ctc_button_book_demo_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_AUTOMOTIVE)
    #time.sleep(2)
    a = Automotive(driver)
    #ma.scroll(3600)
    #ma.close_windows_popup()
    #ma.scroll(300)
    #time.sleep(2)
    a.js_click(a.BOOK_DEMO_BUTTON)
    assert a.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_get_in_touch_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.INDUSTRIES_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.INDUSTRY_AUTOMOTIVE)
    time.sleep(2)
    mp.scroll(3000)
    mp.close_windows_popup()
    time.sleep(2)
    a = Automotive(driver)
    a.js_click(a.GET_IN_TOUCH_BUTTON)
    time.sleep(2)
    assert "https://teldrip.com/contact" in driver.current_url, "Get in Touch button did not redirect to the correct URL"