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
    
    def getCartTotal(self):
        return float(self.browserActions.getText(self.locators.totalAmount))


    def openPaymentForm(self):
        self.browserActions.click(self.locators.placeOrderButton)
        
    def getPaymentTotal(self):
        return float(self.browserActions.getText(self.locators.placeOrderTotal))
      
    def submitPaymentForm(self, paymentInfo):
        self.browserActions.typeInto(self.locators.nameInput, paymentInfo.name)
        self.browserActions.typeInto(self.locators.countryInput, paymentInfo.country)
        self.browserActions.typeInto(self.locators.cityInput, paymentInfo.city)
        self.browserActions.typeInto(self.locators.cardInput, paymentInfo.card)
        self.browserActions.typeInto(self.locators.monthInput, paymentInfo.monthCard)
        self.browserActions.typeInto(self.locators.yearInput, paymentInfo.yearCard)
        self.browserActions.click(self.locators.purchaseButton)
