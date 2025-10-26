from Locators.MainLocator import MainLocator
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver=driver
        self.locator=MainLocator()

    def adminElement(self):
        return self.driver.find_element(By.XPATH, self.locator.adminLocator)

    def jobElement(self):
        return self.driver.find_element(By.XPATH, self.locator.jobLocator)

    def jobTitlesElement(self):
        return self.driver.find_element(By.XPATH, self.locator.jobTitlesLocator)

        