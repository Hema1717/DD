from selenium.webdriver.support.select import Select
from selenium import webdriver

protocol ="https://"
host = "www.dronedeploy.com"
signup_url = protocol+host
chrome_path ="C:/Users/Hema/selenium_drivers/chromedriver.exe"
signup_button_signup_xpath = "//A[@class='btn btn-secondary'][text()='Sign Up']"  # signup on landing page
signup_input_firstname_id = "name" # signup first name
signup_input_lastname_id= "last" # signup last name
signup_input_email_id= "username" # signup email id
signup_input_organization_id= "company" # signup organization name
signup_input_phone_id= "phone" # signup phone number
signup_input_industry_xpath= "(//INPUT[@type='text'])[4]"
signup_input_industry_xpath1 = "//select[@name='industry']" # clicking on input
signup_slect_industryother_xpath = "//SPAN[text()='Other']"
signup_input_password_id= "password" # signup password
signup_input_confirmpassword_id= "confirm_password" # signup  confirm password
signup_button_submit_id="submit" # signup submit

