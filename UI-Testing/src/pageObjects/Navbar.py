from src.locators.NavbarLocators import NavbarLocators
from src.pageObjects.Base import Base
class Navbar (Base):
    locators = NavbarLocators()

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)