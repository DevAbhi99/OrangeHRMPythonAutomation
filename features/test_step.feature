Feature: Test the Job titles for QA in OrangeHRM

Scenario Outline: To test the login function of the website
Given the user is on the login page
When the user puts the valid username "<username>" and password "<password>"
And the user clicks on the login button
Then the user is navigated to the landing page

Examples:
  | username | password |
  | Admin    | admin123 |


Scenario: To test the job titles page and capture the job titles
Given the user is on the landing page of the website
When the user clicks on the admin tab and then on the Jobs tab
And the user clicks on the jobTitles tab
Then the user is displayed all the job titles


Scenario: To test the logout functionality
Given the user is on the landing page of the website
When the user clicks on the profile tab
And the user clicks on the logout button
Then the user is logged out of the website
