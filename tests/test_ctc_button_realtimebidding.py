import time
from pages.main_page import MainPage
from pages.real_time_bidding_page import RealTimeBidding

def test_ctc_button_schedule_demo_real_time_bidding(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.INSIGHTS_REAL_TIME_BIDDING)
    rtb = RealTimeBidding(driver)
    time.sleep(2)
    rtb.click_schedule_demo()
    assert rtb.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_request_demo_real_time_bidding(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.INSIGHTS_REAL_TIME_BIDDING)
    time.sleep(2)
    rtb = RealTimeBidding(driver)
    time.sleep(2)
    rtb.scroll(3500)
    rtb.close_windows_popup()
    rtb.scroll(300)
    time.sleep(2)
    rtb.js_click(rtb.REQUEST_DEMO_BUTTON)
    assert rtb.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_subscribe_real_time_bidding(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.INSIGHTS_REAL_TIME_BIDDING)
    time.sleep(2)
    rtb = RealTimeBidding(driver)
    rtb.scroll(3500)
    rtb.close_windows_popup()
    rtb.scroll(1500)
    time.sleep(2)
    rtb.write(rtb.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    rtb.click_subscribe()
    assert rtb.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"