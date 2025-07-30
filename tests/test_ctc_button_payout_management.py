import time
from pages.main_page import MainPage
from pages.payout_management_page import PayoutManagement


def test_ctc_button_schedule_demo_payout_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.INSIGHT_PAYOUT_MANAGEMENT)
    pm = PayoutManagement(driver)
    pm.click_schedule_demo()
    assert pm.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_request_demo_payout_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.INSIGHT_PAYOUT_MANAGEMENT)
    pm = PayoutManagement(driver)
    time.sleep(2)
    pm.scroll(3000)
    pm.close_windows_popup()
    pm.scroll(800)
    time.sleep(2)
    pm.js_click(pm.REQUEST_DEMO_BUTTON)
    assert pm.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_subscribe_payout_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.INSIGHT_PAYOUT_MANAGEMENT)
    time.sleep(2)
    pm = PayoutManagement(driver)
    pm.scroll(3000)
    pm.close_windows_popup()
    pm.scroll_to_element(pm.SUBSCRIBE_EMAIL)
    time.sleep(2)
    pm.write(pm.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    pm.click_subscribe()
    assert pm.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"