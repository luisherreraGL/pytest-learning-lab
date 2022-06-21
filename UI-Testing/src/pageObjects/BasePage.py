from src.pageObjects.Base import Base

class BasePage (Base):
    path = ""
    title = ""

    def __init__(self, browserActions) -> None:
       self.browserActions =  browserActions

    def open(self):
        self.browserActions.navigateWithBaseurl(self.path)
        #quitar baseurl
        #wait logic 