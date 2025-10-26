from Pages.LogoutPages import LogoutPage

class LogoutController:
    def __init__(self, driver):
        self.driver=driver
        self.page=LogoutPage()


    def profileClick(self):
        return self.page.profileElement().click()

    def logoutClick(self):
        return self.page.logoutElement().click()