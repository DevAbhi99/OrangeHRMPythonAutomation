import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Controllers.LoginController import LoginController
from Controllers.MainController import MainController
from Controllers.LogoutController import LogoutController
from pytest_bdd import scenarios, given, when, then, parsers
import time

# Load all scenarios from the feature file
scenarios('features/test_step.feature')


# Fixtures for browser setup and teardown
@pytest.fixture
def browser():
    """Initialize the browser before each scenario and quit after"""
    baseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    service = Service(executable_path="chromedriver.exe")
    opts = webdriver.ChromeOptions()
    opts.add_argument("--proxy-server='direct://'")
    opts.add_argument("--proxy-bypass-list=*")
    opts.add_argument("--disable-quic")
    opts.set_capability("acceptInsecureCerts", True)
    
    driver = webdriver.Chrome(service=service, options=opts)
    driver.get(baseUrl)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown - quit the browser after the scenario
    time.sleep(1)
    driver.quit()


@pytest.fixture
def controllers(browser):
    """Initialize all controllers with the browser instance"""
    return {
        'login': LoginController(browser),
        'main': MainController(browser),
        'logout': LogoutController(browser)
    }


# Step definitions for Login Scenario
@given('the user is on the login page')
def user_on_login_page(browser):
    """User is on the login page"""
    print('The user is on the login page')
    time.sleep(1)


@when(parsers.parse('the user puts the valid username "{username}" and password "{password}"'))
def enter_credentials(browser, controllers, username, password):
    """Enter username and password"""
    time.sleep(1)
    controllers['login'].usernameFill(username)
    time.sleep(1)
    controllers['login'].passwordFill(password)
    time.sleep(1)


@when('the user clicks on the login button')
def click_login_button(browser, controllers):
    """Click the login button"""
    controllers['login'].loginClick()
    time.sleep(2)


@then('the user is navigated to the landing page')
def verify_landing_page(browser):
    """Verify user is on the landing page"""
    time.sleep(1)
    print('Navigated to the landing page')


# Step definitions for Job Titles Scenario
@given('the user is on the landing page of the website')
def user_on_landing_page(browser):
    """User is on the landing page"""
    time.sleep(1)
    print('The user is on the landing page!')


@when('the user clicks on the admin tab and then on the Jobs tab')
def click_admin_and_jobs(browser, controllers):
    """Click admin and jobs tabs"""
    time.sleep(1)
    controllers['main'].adminClick()
    time.sleep(2)
    controllers['main'].jobClick()
    time.sleep(1)


@when('the user clicks on the jobTitles tab')
def click_job_titles(browser, controllers):
    """Click job titles tab"""
    controllers['main'].jobTitlesClick()
    time.sleep(2)


@then('the user is displayed all the job titles')
def verify_job_titles_displayed(browser):
    """Verify job titles are displayed"""
    browser.save_screenshot('screenshots/titles.png')
    time.sleep(1)
    print('Job titles are displayed')


# Step definitions for Logout Scenario
@when('the user clicks on the profile tab')
def click_profile_tab(browser, controllers):
    """Click the profile tab"""
    time.sleep(1)
    controllers['logout'].profileClick()
    time.sleep(1)


@when('the user clicks on the logout button')
def click_logout_button(browser, controllers):
    """Click the logout button"""
    time.sleep(1)
    controllers['logout'].logoutClick()
    time.sleep(1)


@then('the user is logged out of the website')
def verify_logged_out(browser):
    """Verify user is logged out"""
    time.sleep(2)
    browser.save_screenshot("screenshots/confirmed_loggedout.png")
    time.sleep(1)
    print('User is logged out successfully')
