from Pages.LoginPages import LoginPages


class LoginController:
    def __init__(self, driver):
        self.driver=driver
        self.page=LoginPages()

    
    def usernameFill(self, username):
        return self.page.usernameElement().send_keys(username)

    
    def passwordFill(self, password):
        return self.page.passwordElement().send_keys(password)

    def loginClick(self):
        return self.page.loginBtnElement().click()

        