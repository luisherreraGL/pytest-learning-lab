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

    @step("Open Product : {1}")
    def openProduct(self, productName):
        element = self.browserActions.findElementInside(self.locators.productsTable, self.locators.productLink(productName))
        self.browserActions.scrollTo(element)
        element.click()

    @step("Select Category : {1}")
    def selectCategory(self, category):
        element = self.browserActions.findElementInside(self.locators.productsSectionContainer, self.locators.productCategoryLink(category))
        self.browserActions.scrollTo(element)
        element.click()

    @step("Open last product page")
    def openLastProduct(self):
        self.browserActions.pauseExecution(3)

        products = self.browserActions.findElements(self.locators.productsContainers)
        lastProduct = products[-1]
        productLink = self.browserActions.findInsideElement(lastProduct, self.locators.product_link)
        productLink.click()