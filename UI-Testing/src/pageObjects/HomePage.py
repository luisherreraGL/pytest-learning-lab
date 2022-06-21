from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.HomeLocators import HomeLocators

class HomePage (BasePage):
    locators = HomeLocators()
    path = "/"
    
    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)
