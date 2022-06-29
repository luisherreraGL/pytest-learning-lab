import time
import pytest
import allure
from src.pageObjects.HomePage import HomePage
from src.pageObjects.ProductPage import ProductPage
from src.pageObjects.CartPage import CartPage
from src.assertions.ProductAssertions import ProductAssertions

@allure.suite("Cart Validation")
@allure.sub_suite('Cart')
@pytest.mark.cart
class CartTests:
    productAssertions = ProductAssertions()

    @allure.description("Add items to cart")
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_items(self, browserActions):
        expectedTextAlert = "Product added"
        addedProducts = []
        homePage = HomePage(browserActions)
        homePage.open()
        homePage.selectCategory("Laptops")
        homePage.openLastProduct()
        productPage = ProductPage(browserActions)
        productPage.waitUntilPageLoaded()
        productInfo = productPage.getProductData()
        addedProducts.append(productInfo)
        productPage.addProduct2Cart()

        alertText = productPage.getAlertText()
        assert alertText == expectedTextAlert

        
        homePage.open()
        homePage.selectCategory("Monitors")
        homePage.openLastProduct()

        productPage.waitUntilPageLoaded()
        productInfo = productPage.getProductData()
        # addedProducts.append(productInfo)
        productPage.addProduct2Cart()

        alertText = productPage.getAlertText()
        assert alertText == expectedTextAlert
        productPage.navbar.clickOnLink("Cart")
        cartPage = CartPage(browserActions)
        cartPage.waitUntilPageLoaded()
        cartItems = cartPage.getProductsData()
        for item in cartItems:
            print(item.name)
            print(item.price)
       
        self.productAssertions.equalLists(cartItems, addedProducts)

        time.sleep(3)
