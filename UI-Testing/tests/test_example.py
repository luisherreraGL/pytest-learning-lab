import pytest
from selenium.webdriver.common.by import By
from src.pageObjects.HomePage import HomePage
import allure

@pytest.fixture
def beforeTest():
    print("beforeTest")
    yield
    print("afterTest")

@allure.description("Example Testing for Demo")
@allure.severity(severity_level="LOW")
def test_example(browserActions, beforeTest):
    print("TEST")
    homePage = HomePage(browserActions)
    homePage.open()
    homePage.navbar.clickOnContact()
