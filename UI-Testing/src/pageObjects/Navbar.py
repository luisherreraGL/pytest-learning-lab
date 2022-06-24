from src.locators.NavbarLocators import NavbarLocators
from src.pageObjects.Base import Base
from allure import step
class Navbar (Base):
    locators = NavbarLocators()

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)

    @step("Click on Contact Link")
    def clickOnContact(self):
        self.browserActions.click(self.locators.contactUsingLink)
