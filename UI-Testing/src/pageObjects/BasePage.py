from src.pageObjects.Base import Base
from allure import step

class BasePage (Base):
    path = ""
    title = ""

    def __init__(self, browserActions) -> None:
       self.browserActions =  browserActions

    def open(self):
        self._open(self.path)
        
    @step("Load the page {1}")
    def _open(self, path):
        self.browserActions.navigateWithBaseurl(path)
        self.waitUntilPageLoaded()

    def waitUntilPageLoaded(self):
         self._waitUntilPageLoaded(self.path);
        
    @step("Wait until page is loaded: {1}")
    def _waitUntilPageLoaded(self, path):
         self.browserActions.waitForPageLoaded(path, self.title);

    def getAlertText(self):
        alertText = self.browserActions.getAlertText()
        self.browserActions.closeAlert()
        return alertText