from selenium.webdriver.common.by import By

class CartLocators:
  modalContainer = (By.ID, "orderModal")
  totalAmount =  (By.ID, "totalp")
  tableRows =  (By.CSS_SELECTOR, "#tbodyid tr")
  nameColumn = (By.CSS_SELECTOR, "td:nth-child(2)")
  priceColumn = (By.CSS_SELECTOR, "td:nth-child(3)")
  placeOrderButton = (By.CSS_SELECTOR, 'button[data-toggle="modal"]')
  # Payment form
  placeOrderTotal = (By.ID, "totalm")
  nameInput = (By.ID, "name")
  countryInput = (By.ID, "country")
  cityInput = (By.ID, "city")
  cardInput = (By.ID, "card")
  monthInput = (By.ID, "month")
  yearInput = (By.ID, "year")
  purchaseButton = (By.CSS_SELECTOR, "#orderModal  .btn-primary")
