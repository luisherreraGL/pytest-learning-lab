from src.pageObjects.HomePage import HomePage
from src.pageObjects.ProductPage import ProductPage
from allure import step
from src.assertions.CommonAssertions import CommonAssertions

@step("Adding last product from {1} category to cart")
def addLastProduct2CartSteps(browserActions, category):
    expectedTextAlert = "Product added"
    homePage = HomePage(browserActions)
    homePage.open()
    homePage.selectCategory(category)
    homePage.openLastProduct()
    productPage = ProductPage(browserActions)
    productPage.waitUntilPageLoaded()
    productInfo = productPage.getProductData()
    productPage.addProduct2Cart()

    alertText = productPage.getAlertText()
    productPage.closeAlert()
    CommonAssertions().assertEqualString(expectedTextAlert, alertText, "Alert text")


    return productInfo