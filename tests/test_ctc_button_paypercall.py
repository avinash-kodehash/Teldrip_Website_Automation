import time
from pages.main_page import MainPage
from pages.pay_per_call_page import PayPerCall

def test_ctc_button_schedule_demo_pay_per_call(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.INSIGHTS_PAY_PER_CALL)
    ppc = PayPerCall(driver)
    time.sleep(2)
    ppc.click_schedule_demo()
    assert ppc.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_request_demo_pay_per_call(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.INSIGHTS_PAY_PER_CALL)
    ppc = PayPerCall(driver)
    time.sleep(2)
    ppc.scroll(3500)
    ppc.close_windows_popup()
    ppc.scroll(900)
    time.sleep(2)
    ppc.js_click(ppc.REQUEST_DEMO_BUTTON)
    assert ppc.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_subscribe_pay_per_call(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.INSIGHTS_PAY_PER_CALL)
    time.sleep(2)
    ppc = PayPerCall(driver)
    ppc.scroll(3500)
    ppc.close_windows_popup()
    ppc.scroll_to_element(ppc.SUBSCRIBE_EMAIL)
    time.sleep(2)
    ppc.write(ppc.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    ppc.click_subscribe()
    assert ppc.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"