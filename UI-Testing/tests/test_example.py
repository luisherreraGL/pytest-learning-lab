import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def beforeTest():
    print("beforeTest")
    yield
    print("afterTest")

def test_example(browserActions, beforeTest):
    print("TEST")
    browserActions.navigateTo("http://www.python.org")
    locator = (By.NAME, "q")
    browserActions.type_into(locator,"pycon" )
