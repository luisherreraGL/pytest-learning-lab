from src.pageObjects.Base import Base
from allure import step

class BasePage (Base):
    path = ""
    title = ""

    def __init__(self, browserActions) -> None:
       self.browserActions =  browserActions

    @step("Load the page")
    def open(self):
        self.browserActions.navigateWithBaseurl(self.path)
        #quitar baseurl
        #wait logic 