from selenium.webdriver.common.by import By

class ProductLocators:
    name = (By.TAG_NAME, "h2")
    price = (By.TAG_NAME, "h3")
    addButton = (By.LINK_TEXT, "Add to cart")