import pytest
from selenium.webdriver.common.by import By
from src.pageObjects.HomePage import HomePage
import time

@pytest.fixture
def beforeTest():
    print("beforeTest")
    yield
    print("afterTest")

def test_example(browserActions, beforeTest):
    print("TEST")
    homePage = HomePage(browserActions)
    homePage.open()
    homePage.navbar.clickOnContact()
    time.sleep(5)
