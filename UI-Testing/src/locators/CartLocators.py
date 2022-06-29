from selenium.webdriver.common.by import By

class CartLocators:
  totalAmount =  (By.ID, "totalp")
  tableRows =  (By.CSS_SELECTOR, "#tbodyid tr")
  nameColumn = (By.CSS_SELECTOR, "td:nth-child(2)")
  priceColumn = (By.CSS_SELECTOR, "td:nth-child(3)")
