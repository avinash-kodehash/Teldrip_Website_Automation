import time

from pages.call_reporting_page import CallReporting
from pages.insights_call_tracking_page import CallTracking
from pages.main_page import MainPage


def test_ctc_button_schedule_demo_call_reporting(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHT_CALL_REPORTING)
    cr = CallReporting(driver)
    time.sleep(2)
    cr.zoom_control(75)
    cr.click_schedule_demo()
    assert cr.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_request_demo_call_reporting(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHT_CALL_TRACKING)
    cr = CallReporting(driver)
    time.sleep(2)
    cr.scroll(3500)
    cr.close_windows_popup()
    cr.scroll(2400)
    time.sleep(2)
    cr.click_request_demo()
    assert cr.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_subscribe_call_reporting(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHT_CALL_TRACKING)
    cr = CallReporting(driver)
    time.sleep(2)
    cr.scroll(3500)
    cr.close_windows_popup()
    cr.scroll(3500)
    time.sleep(2)
    cr.write(cr.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    cr.click_subscribe()
    assert cr.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"