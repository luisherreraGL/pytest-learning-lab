import pytest
import allure
from src.pageObjects.HomePage import HomePage
from src.pageObjects.ProductPage import ProductPage
from src.pageObjects.CartPage import CartPage
from src.assertions.ProductAssertions import ProductAssertions
from src.sharedSteps.ProductSteps import addLastProduct2CartSteps
from src.models.PaymentInfo import PaymentInfo
from src.assertions.PaymentConfirmationAssertions import PaymentConfirmationAssertions
from src.assertions.CommonAssertions import CommonAssertions

@allure.suite("Cart Validation")
@allure.sub_suite('Cart')
@pytest.mark.cart
class CartTests:
    productAssertions = ProductAssertions()
    paymentConfirmationAssertions = PaymentConfirmationAssertions()
    commonAssertions = CommonAssertions()

    @allure.description("Add items to cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_items(self, browserActions):
        addedProducts = []
        productPage = ProductPage(browserActions)
        
        addedProducts.append(addLastProduct2CartSteps(browserActions, "Laptops"))
        addedProducts.append(addLastProduct2CartSteps(browserActions, "Monitors"))

        productPage.navbar.clickOnLink("Cart")
        cartPage = CartPage(browserActions)
        cartPage.waitUntilPageLoaded()

        cartItems = cartPage.getProductsData()
        cartTotal = cartPage.getCartTotal()
        self.productAssertions.equalLists(cartItems, addedProducts)
        self.productAssertions.priceSumIsEqual(addedProducts, cartTotal)

    @allure.description("Buy items in cart")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.debug
    def test_buy_items(self, browserActions):
        addedProducts = []
        productPage = ProductPage(browserActions)
        paymentInfo = PaymentInfo("Leo", "Costa Rica", "Heredia", "99999999", 7, 2022)

        expectedThanksMessage = "Thank you for your purchase!"
   
        addedProducts.append(addLastProduct2CartSteps(browserActions, "Laptops"))
        addedProducts.append(addLastProduct2CartSteps(browserActions, "Monitors"))

        productPage.navbar.clickOnLink("Cart")
        cartPage = CartPage(browserActions)
        cartPage.waitUntilPageLoaded()

        cartTotal = cartPage.getCartTotal()
        cartPage.openPaymentForm()

        paymentTotal = cartPage.getPaymentTotal()
        self.commonAssertions.assertEqualString(paymentTotal, cartTotal, "Payment Total")

        cartPage.submitPaymentForm(paymentInfo)

        thankMessage = cartPage.getPaymentConfirmationHeader()
        self.commonAssertions.assertEqualString(thankMessage, expectedThanksMessage, "Thanks message")

        paymentConfirmationDetails = cartPage.getPaymentConfirmationDetails()
        self.paymentConfirmationAssertions.validateConfirmationDetails(paymentInfo, paymentTotal, paymentConfirmationDetails)

        cartPage.closePaymentForm()

        homePage = HomePage(browserActions)

        homePage.waitUntilPageLoaded()