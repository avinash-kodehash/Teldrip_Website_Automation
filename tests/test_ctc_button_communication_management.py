import time
from pages.connect_communication_management_page import CommunicationManagement
from pages.main_page import MainPage

def test_ctc_button_schedule_demo_communication_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_COMMUNICATION_MANAGEMENT)
    cm = CommunicationManagement(driver)
    time.sleep(2)
    cm.click_schedule_demo()
    assert cm.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_book_demo_communication_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_COMMUNICATION_MANAGEMENT)
    time.sleep(2)
    cm = CommunicationManagement(driver)
    time.sleep(2)
    cm.scroll(2500)
    cm.close_windows_popup()
    cm.scroll(300)
    time.sleep(2)
    cm.js_click(cm.BOOK_DEMO_BUTTON)
    assert cm.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_see_how_connect_works_communication_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_COMMUNICATION_MANAGEMENT)
    time.sleep(2)
    cm = CommunicationManagement(driver)
    time.sleep(2)
    cm.scroll(2500)
    cm.close_windows_popup()
    cm.scroll(300)
    time.sleep(2)
    cm.do_click(cm.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    assert cm.driver.current_url == "https://teldrip.com/contact"

def test_ctc_button_subscribe_communication_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_COMMUNICATION_MANAGEMENT)
    time.sleep(2)
    cm = CommunicationManagement(driver)
    cm.scroll(3500)
    cm.close_windows_popup()
    cm.scroll(1500)
    time.sleep(2)
    cm.write(cm.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    cm.click_subscribe()
    assert cm.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"