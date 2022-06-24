from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BrowserActions:
    defaultWaitTimeSeconds = 10

    def __init__(self, driver, baseurl) -> None:
        self.driver = driver
        self.baseurl = baseurl
    
    def navigateWithBaseurl(self, path):
        self.navigateTo(self.baseurl + path)

    def navigateTo(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.waitForAvailability(locator)
        element = self.findElement(locator)
        element.click()

    def type_into(self, locator, text):
        self.waitForAvailability(locator)
        element = self.findElement(locator)
        element.clear()
        element.send_keys(text)

    def findElement(self, locator):
        return  self.driver.find_element(*locator)

    def waitForAvailability (self, locator):
        errorMessage =  'Element with the locator {0} is not available (it should exist in the DOM, visible & enabled)'.format(locator)

        wait = WebDriverWait(self.driver, self.defaultWaitTimeSeconds)
        wait.until(EC.visibility_of_element_located(locator), errorMessage)
        wait.until(EC.element_to_be_clickable(locator), errorMessage)


