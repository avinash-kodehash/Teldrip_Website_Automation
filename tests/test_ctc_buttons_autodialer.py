import time

from pages.connect_autodialer_page import AutoDialer
from pages.main_page import MainPage

def test_ctc_button_schedule_demo_autodialer(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_AUTODIALER)
    ad = AutoDialer(driver)
    time.sleep(2)
    ad.click_schedule_demo()
    assert ad.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_book_demo_autodialer(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_AUTODIALER)
    time.sleep(2)
    ad = AutoDialer(driver)
    time.sleep(2)
    ad.scroll(3000)
    ad.close_windows_popup()
    ad.scroll(300)
    time.sleep(2)
    ad.js_click(ad.BOOK_DEMO_BUTTON)
    assert ad.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_see_how_connect_works_autodialer(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_AUTODIALER)
    time.sleep(2)
    ad = AutoDialer(driver)
    time.sleep(2)
    ad.scroll(3000)
    ad.close_windows_popup()
    ad.scroll(300)
    time.sleep(2)
    ad.do_click(ad.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    assert ad.driver.current_url == "https://teldrip.com/contact"

def test_ctc_button_subscribe_autodialer(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_AUTODIALER)
    time.sleep(2)
    ad = AutoDialer(driver)
    ad.scroll(3500)
    ad.close_windows_popup()
    ad.scroll_to_element(ad.SUBSCRIBE_EMAIL)
    time.sleep(2)
    ad.write(ad.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    ad.click_subscribe()
    assert ad.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"