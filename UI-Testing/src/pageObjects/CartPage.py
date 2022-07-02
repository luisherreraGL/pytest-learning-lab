from src.pageObjects.BasePage import BasePage
from src.pageObjects.Navbar import Navbar
from src.locators.CartLocators import CartLocators
from allure import step
from src.models.Product import Product
from allure import step

class CartPage (BasePage):
    locators = CartLocators()
    path = "/cart.html"
    title = "STORE"

    def __init__(self, browserActions) -> None:
        super().__init__(browserActions)
        self.navbar = Navbar(browserActions)

    def open(self):
        super().open()
        self.browserActions.pauseExecution(3)

    @step("Getting all cart items data")
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
    
    @step("Getting buy Total Amount")
    def getCartTotal(self):
        return float(self.browserActions.getText(self.locators.totalAmount))

    @step("Opening Payment form")
    def openPaymentForm(self):
        self.browserActions.click(self.locators.placeOrderButton)
        
    @step("Getting payment Total Amount")
    def getPaymentTotal(self):
        totalOrder = self.browserActions.getText(self.locators.placeOrderTotal)
        return float(totalOrder.split()[1])
    
    @step("Submiting payment")
    def submitPaymentForm(self, paymentInfo):
        divWithScrollContainer = self.locators.modalContainer
        self.browserActions.typeInto(self.locators.nameInput, paymentInfo.name, divWithScrollContainer)
        self.browserActions.typeInto(self.locators.countryInput, paymentInfo.country, divWithScrollContainer)
        self.browserActions.typeInto(self.locators.cityInput, paymentInfo.city, divWithScrollContainer)
        self.browserActions.typeInto(self.locators.cardInput, paymentInfo.card, divWithScrollContainer)
        self.browserActions.typeInto(self.locators.monthInput, paymentInfo.monthCard, divWithScrollContainer)
        self.browserActions.typeInto(self.locators.yearInput, paymentInfo.yearCard, divWithScrollContainer)
        self.browserActions.click(self.locators.purchaseButton, divWithScrollContainer)

    @step("Gettig payment confirmation details")
    def getPaymentConfirmationDetails(self):
        return self.browserActions.getText(self.locators.paymentDetails)

    def getPaymentConfirmationHeader(self):
        return self.browserActions.getText(self.locators.thanksMessage)

    @step("Closing payment confirmation")
    def closePaymentForm(self):
        self.browserActions.click(self.locators.okButton)
