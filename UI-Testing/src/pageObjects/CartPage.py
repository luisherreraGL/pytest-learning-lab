from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.CartLocators import CartLocators
from allure import step
from src.models.Product import Product

class CartPage (BasePage):
    locators = CartLocators()
    path = "/cart.html"
    title = "STORE"

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)

    def getProductsData(self):
        productList = []
        self._waitForTableProducts()
        products = self.browserActions.findElements(self.locators.tableRows)

        for product in products:
            nameColumn = self.browserActions.findInsideElement(product, self.locators.nameColumn)
            priceColumn = self.browserActions.findInsideElement(product, self.locators.priceColumn)
            productList.append(Product(nameColumn.text, float(priceColumn.text)))

        return productList

    def _waitForTableProducts(self):
        def customCondition (driver):
            products = self.browserActions.findElements(self.locators.tableRows)
            return len(products) > 0
    
        self.browserActions.waitFor([customCondition], "The page did not renders the products")