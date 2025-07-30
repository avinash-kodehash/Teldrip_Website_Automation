import time
from pages.connect_workforce_management_page import WorkforceManagement
from pages.main_page import MainPage

def test_ctc_button_schedule_workforce_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_WORKFORCE_MANAGEMENT)
    vm = WorkforceManagement(driver)
    time.sleep(2)
    vm.click_schedule_demo()
    assert vm.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_book_demo_workforce_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_WORKFORCE_MANAGEMENT)
    time.sleep(2)
    vm = WorkforceManagement(driver)
    vm.scroll(4000)
    vm.close_windows_popup()
    vm.scroll(300)
    time.sleep(2)
    vm.js_click(vm.BOOK_DEMO_BUTTON)
    assert vm.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_see_how_connect_works_workforce_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_WORKFORCE_MANAGEMENT)
    time.sleep(2)
    vm = WorkforceManagement(driver)
    vm.scroll(4000)
    vm.close_windows_popup()
    vm.scroll(300)
    time.sleep(2)
    vm.js_click(vm.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    assert vm.driver.current_url == "https://teldrip.com/contact"

def test_ctc_button_subscribe_workforce_management(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_WORKFORCE_MANAGEMENT)
    time.sleep(2)
    vm = WorkforceManagement(driver)
    vm.scroll(3500)
    vm.close_windows_popup()
    vm.scroll_to_element(vm.SUBSCRIBE_EMAIL)
    time.sleep(2)
    vm.write(vm.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    vm.click_subscribe()
    assert vm.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"