from src.pageObjects.HomePage import HomePage
from src.pageObjects.ProductPage import ProductPage

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
    assert alertText == expectedTextAlert

    return productInfo