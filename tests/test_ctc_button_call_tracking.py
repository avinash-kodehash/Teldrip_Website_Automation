import time

from pages.insights_call_tracking_page import CallTracking
from pages.main_page import MainPage


def test_ctc_button_schedule_demo_call_tracking(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.do_click(mp.INSIGHT_CALL_TRACKING)
    mp.zoom_control(75)
    ct = CallTracking(driver)
    ct.click_schedule_demo()
    assert ct.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_request_demo_call_tracking(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHT_CALL_TRACKING)
    ct = CallTracking(driver)
    time.sleep(2)
    ct.scroll(3500)
    ct.close_windows_popup()
    ct.scroll(2200)
    time.sleep(2)
    ct.js_click(ct.REQUEST_DEMO_BUTTON)
    assert ct.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_subscribe_call_tracking(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHT_CALL_TRACKING)
    ct = CallTracking(driver)
    time.sleep(2)
    ct.scroll(3500)
    ct.close_windows_popup()
    ct.scroll_to_element(ct.SUBSCRIBE_EMAIL)
    time.sleep(2)
    ct.write(ct.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    ct.click_subscribe()
    assert ct.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"