from src.pageObjects.Base import Base

class BasePage (Base):
    baseurl = "https://demoblaze.com"
    path = ""

    def __init__(self, browserActions) -> None:
       self.browserActions =  browserActions

    def open(self):
        self.browserActions.navigateTo(self.baseurl + self.path)