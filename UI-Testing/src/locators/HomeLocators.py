from selenium.webdriver.common.by import By
class HomeLocators:
    productsContainers = (By.CSS_SELECTOR, "#tbodyid div")
    productsSectionContainer =  (By.ID, "contcont")

    productsImages = (By.CSS_SELECTOR, "#tbodyid img")
    paginationNextButton = (By.CSS_SELECTOR, ".pagination #next2")
    productsTable = (By.ID, "tbodyid")
    product_link = (By.CSS_SELECTOR, "a")
    
    def productLink(self, productName):
        return (By.PARTIAL_LINK_TEXT, productName)

    def productCategoryLink(self, category):
        return (By.LINK_TEXT, category)

