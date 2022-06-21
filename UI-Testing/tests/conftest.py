import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.utils.BrowserActions import BrowserActions

@pytest.fixture
def browserActions():
    print("setup browserActions")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browserActions = BrowserActions(driver)
    yield browserActions
    print("teardown browserActions")
    driver.close()