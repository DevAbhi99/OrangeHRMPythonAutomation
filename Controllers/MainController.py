from Pages.MainPages import MainPage


class MainController:

    def __init__(self, driver):
        self.driver=driver
        self.page=MainPage(self.driver)

    
    def adminClick(self):
        return self.page.adminElement.click()

    def jobClick(self):
        return self.page.jobElement.click()

    def jobTitlesClick(self):
        return self.page.jobTitlesElement.click()

    
