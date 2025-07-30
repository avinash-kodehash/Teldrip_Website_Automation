import time
from pages.connect_campaign_page import Campaign
from pages.main_page import MainPage

def test_ctc_button_schedule_campaign(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_CAMPAIGN)
    c = Campaign(driver)
    time.sleep(2)
    c.click_schedule_demo()
    assert c.is_calender_displayed(), "Calendar is not displayed after clicking Schedule Demo button"

def test_ctc_button_book_demo_campaign(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_CAMPAIGN)
    time.sleep(2)
    c = Campaign(driver)
    time.sleep(2)
    c.scroll(3000)
    c.close_windows_popup()
    c.scroll(300)
    time.sleep(2)
    c.js_click(c.BOOK_DEMO_BUTTON)
    assert c.is_calender_displayed(), "Calendar is not displayed after clicking Request Demo button"

def test_ctc_button_see_how_connect_works_campaign(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_CAMPAIGN)
    #time.sleep(2)
    c = Campaign(driver)
    time.sleep(2)
    c.scroll(3000)
    c.close_windows_popup()
    c.scroll_to_element(c.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    c.js_click(c.SEE_HOW_CONNECT_WORKS)
    time.sleep(2)
    assert c.driver.current_url == "https://teldrip.com/contact"

def test_ctc_button_subscribe_campaign(driver):
    driver = driver
    mp = MainPage(driver)
    mp.do_click(mp.PRODUCTS_LINK)
    mp.zoom_control(75)
    time.sleep(2)
    mp.do_click(mp.CONNECT_CAMPAIGN)
    time.sleep(2)
    c = Campaign(driver)
    c.scroll(3500)
    c.close_windows_popup()
    c.scroll_to_element(c.SUBSCRIBE_EMAIL)
    time.sleep(2)
    c.write(c.SUBSCRIBE_EMAIL,"Automation@gmail.com")
    c.click_subscribe()
    assert c.is_subscribe_popup_displayed(), "Subscribe popup is not displayed after clicking Subscribe button"