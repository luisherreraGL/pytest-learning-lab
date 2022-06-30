from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.AutoScrollHelper import AutoScrollHelper
from selenium.webdriver.common.alert import Alert

class BrowserActions:
    _DEFAULT_WAIT_TIME_SECONDS = 10
    _DEFAULT_NAVBAR_HEIGHT = 0
    _DEFAULT_FOOTER_HEIGHT = 0

    def __init__(self, driver, baseurl) -> None:
        self.driver = driver
        self.baseurl = baseurl
        self.autoScrollHelper = AutoScrollHelper(driver, self._DEFAULT_NAVBAR_HEIGHT, self._DEFAULT_FOOTER_HEIGHT)
        self.alert = Alert(driver)

    def getAlertText (self):
        alert = self.waitFor([EC.alert_is_present()])
        return self.alert.text

    def closeAlert(self):
        self.alert.accept()

    def navigateWithBaseurl(self, path):
        self.navigateTo(self.baseurl + path)

    def navigateTo(self, url):
        self.driver.get(url)

    def waitForPageLoaded(self, path, title):
        expectedUrl = self.baseurl + path
        errorMessage = 'waitForPageLoaded error: {0}'.format(expectedUrl)

        customCondition = lambda driver : expectedUrl in driver.current_url and  driver.title == title and self.isDOMReady()  
        self.waitFor([customCondition], errorMessage)

    def isDOMReady(self):
        return self.driver.execute_script("return document.readyState == 'complete'")

    def click(self, locator):
        self.waitForAvailability(locator)
        element = self.findElement(locator)
        self.scrollTo(element)
        element.click()

    def typeInto(self, locator, text):
        self.waitForAvailability(locator)
        element = self.findElement(locator)
        self.scrollTo(element)
        element.clear()
        element.send_keys(text)

    def waitForAvailability(self, locator):
        errorMessage = 'Element with the locator {0} is not available (it exists in the DOM, visible & enabled)'.format(locator)
        conditions = [EC.visibility_of_element_located(locator), EC.element_to_be_clickable(locator)]
        self.waitFor(conditions, errorMessage)

    def scrollTo(self, element):
        self.autoScrollHelper.scrollTo(element)
    
    def findElement(self, locator):
        return self.driver.find_element(*locator)

    def findElements(self, locator):
        return self.driver.find_elements(*locator)

    def findInsideElement(self, element, locator):
        return element.find_element(*locator)
    
    def getText(self, locator):
        conditions = [EC.visibility_of_element_located(locator)]
        self.waitFor(conditions)
        return self.findElement(locator).text

    def waitFor(self, conditions, errorMessage="WaitFor Condition Failed", timeoutSeconds = None):
        timeoutSeconds = timeoutSeconds or self._DEFAULT_WAIT_TIME_SECONDS
        wait = WebDriverWait(self.driver, timeoutSeconds)

        for condition in conditions:
            wait.until(condition, errorMessage)
        
    def isImageLoaded(self, webImageElement):
        return self.driver.execute_script(
            'return arguments[0].complete && arguments[0].naturalHeight !== 0;',
            webImageElement)

    def findElementInside(self, containerLocator, locatorToSearch):
        self.waitForAvailability(containerLocator)
        containerElement =  self.findElement(containerLocator)

        def customCondition (driver):
            try:
                containerElement.find_element(*locatorToSearch)
            except: 
                return False

            return True
        
        self.waitFor([customCondition], "Could find element: {0} inside of {1}".format(locatorToSearch, containerLocator) )
        element = containerElement.find_element(*locatorToSearch)
        self.waitFor([EC.visibility_of(element)], "Element Inside of {0} is not visible".format(containerLocator))

        return element