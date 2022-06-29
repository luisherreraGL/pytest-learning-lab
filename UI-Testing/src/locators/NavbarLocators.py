from selenium.webdriver.common.by import By
class NavbarLocators:
    navbarContainer = (By.ID, "navbarExample")

    def navbarLink(self, linkName):
        return (By.PARTIAL_LINK_TEXT, linkName)