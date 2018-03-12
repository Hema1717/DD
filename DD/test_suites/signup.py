import unittest
from selenium import webdriver
from time import sleep
from dd.page_objects import signup
from dd.utilities.common_utilities import json_testbed_parser
from dd.utilities.ui_utilities import selenium_utilities

class businessUserSignIn(unittest.TestCase):
    def setUp(self):  # code to launch the singin page
        try:
            self.driver = webdriver.Chrome(signup.chrome_path)
            self.driver.implicitly_wait(30)
            self.driver.get(signup.signup_url)  # Register Url
            self.driver.delete_all_cookies()
            self.driver.maximize_window()
            print("1. Application launched successfully  ")
        except:
            self.assertTrue(False, "1.There was an issue while launching the application")

    def test_registeration(self):

        try:
            firstName, lastName, email, organization, phone, password, confirmPassword = json_testbed_parser.get_default_register_credentials()
            selenium_utilities.userRegister(self.driver,firstName,lastName,email,organization,phone,password,confirmPassword)
            text_verification = self.driver.find_element_by_xpath("//path[@id='dronedeploy-drone-svg-icon']").text
            self.assertEquals(text_verification, "Dashboard")  # Text verification text "SIGN IN" from the login page
            print("Successfully registered")
        except:
            self.assertTrue(False,"Registration unsuccessful ")




    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
