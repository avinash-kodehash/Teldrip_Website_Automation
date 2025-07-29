from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def element_displayed(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def take_element_screenshot(self,locator,file_path):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        element.screenshot(file_path)

    def scroll_to_element(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)

    def write(self,locator,text):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)

    def scroll(self,length):
        self.driver.execute_script(f"window.scrollBy(0, {length});")

    def zoom_control(self, zoom_level):
        self.driver.execute_script(f"document.body.style.zoom='{zoom_level}%'")

    def js_click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

