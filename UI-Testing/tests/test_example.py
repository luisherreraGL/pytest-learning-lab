import time
import pytest
import allure
from src.pageObjects.HomePage import HomePage
from src.pageObjects.ProductPage import ProductPage

@allure.suite("Example Test")
@allure.sub_suite('Demo')
@pytest.mark.smoke
class ExampleTests:

    @pytest.fixture(autouse=True)
    def beforeTest(self):
        print("beforeTest")
        yield
        print("afterTest")

    @allure.description("Example Testing for Demo")
    @allure.severity(allure.severity_level.MINOR)
    def test_example(self, browserActions):
        homePage = HomePage(browserActions)
        homePage.open()
        homePage.waitUntilPageRendersTheProducts()
        homePage.clickOnNext()
        time.sleep(2)

    @allure.description("Example Testing for Demo - Fail")
    @allure.severity(allure.severity_level.MINOR)
    def test_example_Fail(self, browserActions):
        homePage = HomePage(browserActions)
        homePage.open()
        homePage.waitUntilPageRendersTheProducts()
        homePage.clickOnNext()
        assert False

    def test_example_navbar(self, browserActions): 
        homePage = HomePage(browserActions)
        homePage.open()
        homePage.navbar.clickOnLink("Contact")
        time.sleep(5)

    def test_example_open_product(self, browserActions):
        homePage = HomePage(browserActions)
        homePage.open()
        homePage.waitUntilPageRendersTheProducts()
        #HTC One M9
        #Samsung galaxy s6
        homePage.openProduct("Samsung galaxy s6")
        productPage = ProductPage(browserActions)
        productPage.waitUntilPageLoaded()
        time.sleep(5)
