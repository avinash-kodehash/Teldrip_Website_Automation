import time
from pages.connect_virtual_phone_number_page import VirtualNumber
from pages.main_page import MainPage

def test_ctc_button_schedule_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
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
    time.sleep(2)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    vn = VirtualNumber(driver)
    vn.scroll(3600)
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
    vn.scroll(3600)
    vn.close_windows_popup()
    vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.SEE_HOW_CONNECT_WORKS)
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
    vn.scroll_to_element(vn.SUBSCRIBE_EMAIL)
    time.sleep(2)
    vn.write(vn.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    vn.click_subscribe()
    assert vn.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"

def test_ctc_button_country_indian_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    #vn.close_windows_popup()
    #vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.INDIA)
    assert "https://teldrip.com/virtual-phone-number/india" in driver.current_url, "India virtual number page is not displayed"

def test_ctc_button_country_australia_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    #vn.close_windows_popup()
    #vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.AUSTRALIA)
    assert "https://teldrip.com/virtual-phone-number/australia" in driver.current_url, "Australia virtual number page is not displayed"

def test_ctc_button_country_canada_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    #vn.close_windows_popup()
    #vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.CANADA)
    assert "https://teldrip.com/virtual-phone-number/canada" in driver.current_url, "Canada virtual number page is not displayed"

def test_ctc_button_country_usa_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    #vn.close_windows_popup()
    #vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.USA)
    assert "https://teldrip.com/virtual-phone-number/usa" in driver.current_url, "Usa virtual number page is not displayed"

def test_ctc_button_country_germany_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    #vn.close_windows_popup()
    #vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.GERMANY)
    assert "https://teldrip.com/virtual-phone-number/germany" in driver.current_url, "Germany virtual number page is not displayed"

def test_ctc_button_country_uae_virtual_number(driver):
        driver = driver
        mp = MainPage(driver)
        mp.do_click(mp.PRODUCTS_LINK)
        time.sleep(2)
        mp.zoom_control(75)
        mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
        time.sleep(2)
        vn = VirtualNumber(driver)
        vn.scroll(3000)
        # vn.close_windows_popup()
        # vn.scroll(300)
        time.sleep(2)
        vn.js_click(vn.UAE)
        assert "https://teldrip.com/virtual-phone-number/uae" in driver.current_url, "uae virtual number page is not displayed"


def test_ctc_button_country_uk_virtual_number(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    time.sleep(2)
    mp.zoom_control(75)
    mp.do_click(mp.CONNECT_VIRTUAL_PHONE_NUMBER)
    time.sleep(2)
    vn = VirtualNumber(driver)
    vn.scroll(3000)
    # vn.close_windows_popup()
    # vn.scroll(300)
    time.sleep(2)
    vn.js_click(vn.UK)
    assert "https://teldrip.com/virtual-phone-number/uk" in driver.current_url, "Uk virtual number page is not displayed"