from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.ProductLocators import ProductLocators
from allure import step
from src.models.Product import Product

class ProductPage (BasePage):
    locators = ProductLocators()
    path = "/prod.html"
    title = "STORE"

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)

    @step("Get product data")
    def getProductData(self):
        name = self.browserActions.getText(self.locators.name)
        price = self.browserActions.getText(self.locators.price)
        return Product(name, self.cleanPrice(price))

    def cleanPrice(self, price):
        priceText =  price[1:]
        return float(priceText.split()[0])

    @step("Adding product to cart")
    def addProduct2Cart(self):
        self.browserActions.click(self.locators.addButton)