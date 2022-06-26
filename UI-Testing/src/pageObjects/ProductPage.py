from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.HomeLocators import HomeLocators
from allure import step

class ProductPage (BasePage):
    locators = None
    path = "/prod.html"
    title = "STORE"

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)