import pytest
from selenium.webdriver.common.by import By
from src.pageObjects.HomePage import HomePage

@pytest.fixture
def beforeTest():
    print("beforeTest")
    yield
    print("afterTest")

def test_example(browserActions, beforeTest):
    print("TEST")
    homePage = HomePage(browserActions)
    homePage.open()
    #......
    browserActions.navigateTo("http://www.python.org")
    locator = (By.NAME, "q")
    browserActions.type_into(locator,"pycon" )
