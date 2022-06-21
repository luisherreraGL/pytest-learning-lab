from src.pageObjects.Base import Base

class BasePage (Base):
    baseurl = "https://demoblaze.com"
    path = ""
    title = ""

    def __init__(self, browserActions) -> None:
       self.browserActions =  browserActions

    def open(self):
        #quitar baseurl
        self.browserActions.navigateTo(self.baseurl + self.path)
        #wait