import time
from pages.main_page import MainPage

def test_ctc_button_request_demo(driver):
    driver = driver
    mp = MainPage(driver)
    mp.click_request_demo()
    assert mp.is_calender_displayed()

def test_ctc_button_schedule_demo(driver):
    driver = driver
    mp = MainPage(driver)
    mp.scroll(300)
    mp.click_schedule_demo()
    assert mp.is_calender_displayed()

def test_ctc_button_see_pricing(driver):
    driver = driver
    mp = MainPage(driver)
    mp.scroll(320)
    mp.click_see_pricing()
    time.sleep(2)
    assert mp.driver.current_url == "https://teldrip.com/pricing"

def test_contact_us_form(driver):
    driver = driver
    mp = MainPage(driver)
    mp.scroll(6000)
    time.sleep(2)
    mp.close_windows_popup()
    mp.scroll(2250)
    time.sleep(2)
    mp.fill_contact_info("John", "Doe", "abc@example.com", "2125551234","This is a test message.")
    mp.click_submit()
    assert mp.is_contact_confirmation_msg_displayed() , "confirmation message is not displayed"

def test_subscribe_button(driver):
    driver = driver
    mp = MainPage(driver)
    mp.scroll(6000)
    time.sleep(2)
    mp.close_windows_popup()
    mp.scroll(3500)
    time.sleep(2)
    mp.write(mp.SUBSCRIBE_EMAIL, "Automation@gmail.com")
    mp.click_subscribe()
    assert mp.is_subscribe_popup_displayed() , "Subscribe popup is not displayed"
