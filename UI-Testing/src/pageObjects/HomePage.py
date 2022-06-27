from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.HomeLocators import HomeLocators
from allure import step

class HomePage (BasePage):
    locators = HomeLocators()
    path = "/"
    title = "STORE"

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)

    @step("Click on the next pagination button")
    def clickOnNext(self):
        self.browserActions.click(self.locators.paginationNextButton)

    @step("Wait for products renderization")
    def waitUntilPageRendersTheProducts(self):
        self._waitForProducts()
        self._waitForProductsImages()

    @step("Open Product : {1}")
    def openProduct(self, productName):
        element = self.browserActions.findElementInside(self.locators.productsTable, self.locators.productLink(productName))
        self.browserActions.scrollTo(element)
        element.click()

    def _waitForProductsImages (self):
        def customCondition (driver):
            images = self.browserActions.findElements(self.locators.productsImages)
            results = map(lambda image: self.browserActions.isImageLoaded(image) ,images)
            results_list = list(results)
            allTrue = all(results_list)

            return  allTrue
    
        self.browserActions.waitFor([customCondition], "The page did not renders the products")

    def _waitForProducts(self):
        def customCondition (driver):
            products = self.browserActions.findElements(self.locators.productsContainers)
            return len(products) > 0
    
        self.browserActions.waitFor([customCondition], "The page did not renders the products")