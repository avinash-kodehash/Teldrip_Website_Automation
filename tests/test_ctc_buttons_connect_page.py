import time
from pages.connect_page import ConnectPage
from pages.main_page import MainPage

def test_ctc_button_request_demo_connect(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    cp.click_request_demo()
    assert cp.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_schedule_demo_connect(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    time.sleep(2)
    cp.scroll(300)
    time.sleep(2)
    cp.click_schedule_demo()
    assert cp.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_see_pricing_connect(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    time.sleep(2)
    cp.scroll(300)
    cp.click_see_pricing()
    time.sleep(2)
    assert cp.driver.current_url == "https://teldrip.com/pricing"

def test_ctc_button_booknow(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    time.sleep(2)
    cp.scroll(3500)
    time.sleep(2)
    cp.do_click(cp.BOOK_NOW_BUTTON)
    assert cp.is_calender_displayed(), "Calendar is not displayed after clicking Book Now button"

def test_contact_us_form_connect(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    time.sleep(2)
    cp.scroll(9000)
    time.sleep(2)
    cp.close_windows_popup()
    cp.scroll(3000)
    time.sleep(2)
    cp.fill_contact_info("John", "Doe", "abc@example.com", "2125551234", "This is a test message.")
    cp.click_submit()
    assert cp.is_contact_confirmation_msg_displayed(), "Contact confirmation message is not displayed"

def test_subscribe_connect(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.do_click(mp.CONNECT)
    cp = ConnectPage(driver)
    time.sleep(2)
    cp.scroll(9000)
    time.sleep(2)
    cp.close_windows_popup()
    cp.scroll(4500)
    time.sleep(2)
    cp.write(cp.SUBSCRIBE_EMAIL, "Automation@gmail.com")
    cp.click_subscribe()
    assert cp.is_subscribe_popup_displayed() , "Subscribe popup is not displayed"
