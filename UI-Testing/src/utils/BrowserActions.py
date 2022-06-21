from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BrowserActions:
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def navigateTo(self, url):
        self.driver.get(url)

    def click(self, locator):
        try:
            self.waitForAvailability(locator)
            element = self.findElement(locator)
            element.click()
        except Exception as e:
            print(e)

    def type_into(self, locator, text):
        try:
            #autoScroll
            self.waitForAvailability(locator)
            element = self.findElement(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(e)

    def findElement(self, locator):
        return  self.driver.find_element(*locator)

    def waitForAvailability (self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(locator))
        wait.until(EC.element_to_be_clickable(locator))


