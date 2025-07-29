import time

from pages.insights_page import InsightPage
from pages.main_page import MainPage

def test_ctc_button_request_demo_insight(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHTS)
    ip = InsightPage(driver)
    ip.click_request_demo()
    assert ip.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_schedule_demo_insight(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHTS)
    ip = InsightPage(driver)
    ip.click_schedule_demo()
    assert ip.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_see_pricing_insight(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHTS)
    ip = InsightPage(driver)
    ip.click_see_pricing()
    time.sleep(2)
    assert ip.driver.current_url == "https://teldrip.com/pricing"

def test_contact_us_form_insight(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHTS)
    ip = InsightPage(driver)
    time.sleep(2)
    ip.scroll(7000)
    time.sleep(2)
    ip.close_windows_popup()
    ip.scroll(2800)
    time.sleep(2)
    ip.fill_contact_info("John", "Doe", "abc@example.com", "2125551234", "This is a test message.")
    ip.click_submit()
    assert ip.is_contact_confirmation_msg_displayed(), "Contact confirmation message is not displayed"

def test_subscribe_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.INSIGHTS)
    ip = InsightPage(driver)
    time.sleep(2)
    ip.scroll(7000)
    time.sleep(2)
    ip.close_windows_popup()
    ip.scroll(4000)
    time.sleep(2)
    ip.write(mp.SUBSCRIBE_EMAIL, "Automation@gmail.com")
    ip.click_subscribe()
    assert ip.is_subscribe_popup_displayed() , "Subscribe popup is not displayed"
