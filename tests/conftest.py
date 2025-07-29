import pytest
import os
import time
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def create_screenshot_dir():
    os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://teldrip.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            test_name = "".join(c if c.isalnum() else "_" for c in item.name)
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.abspath(os.path.join("screenshots", filename))
            try:
                driver.save_screenshot(filepath)
            except Exception as e:
                print(f"[ERROR] Could not capture screenshot: {e}")
                return
            try:
                from pytest_html import extras
                rep.extras = getattr(rep, "extras", [])
                rep.extras.append(extras.image(filepath, mime_type="image/png"))
            except ImportError:
                print("[ERROR] pytest-html is not installed.")