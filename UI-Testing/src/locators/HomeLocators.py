from selenium.webdriver.common.by import By
class HomeLocators:
    productsContainers = (By.CSS_SELECTOR, "#tbodyid div")
    productsImages = (By.CSS_SELECTOR, "#tbodyid img")
    paginationNextButton = (By.CSS_SELECTOR, ".pagination #next2")
    productsTable = (By.ID, "tbodyid")
    
    def productLink(self, productName):
        return (By.PARTIAL_LINK_TEXT, productName)
