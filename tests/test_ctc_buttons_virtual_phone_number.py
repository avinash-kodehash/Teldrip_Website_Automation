import time
from pages.connect_virtual_phone_number_page import VirtualNumber
from pages.main_page import MainPage

def test_ctc_button_schedule_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    vn = VirtualNumber(driver)
    time.sleep(2)
    vn.click_schedule_demo()
    assert vn.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_book_demo_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(4000)
    vn.close_windows_popup()
    vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.BOOK_DEMO_BUTTON)
    assert vn.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_see_how_connect_works_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(4000)
    vn.close_windows_popup()
    vn.scroll(300)
    time.sleep(2)
    vn.do_click(vn.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    assert vn.driver.current_url == "https://teldrip.com/contact"

def test_ctc_button_subscribe_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3500)
    vn.close_windows_popup()
    vn.scroll(1500)
    time.sleep(2)
    vn.write(vn.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    vn.click_subscribe()
    assert vn.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"