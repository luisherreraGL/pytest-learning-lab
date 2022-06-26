from src.locators.NavbarLocators import NavbarLocators
from src.pageObjects.Base import Base
from allure import step
class Navbar (Base):
    locators = NavbarLocators()

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)

    @step("Click on {1} link")
    def clickOnLink(self, linkName):
        element = self.browserActions.findElementInside(self.locators.navbarContainer, self.locators.navbarLink(linkName))
        self.browserActions.scrollTo(element)
        element.click()
