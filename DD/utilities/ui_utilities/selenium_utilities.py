from dd.page_objects import signup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

def userRegister(driver,firstName,lastName,email,organization,phone,password,confirmPassword):
    driver.find_element_by_xpath(signup.signup_button_signup_xpath).click()
    name=firstName
    driver.find_element_by_id(signup.signup_input_firstname_id).send_keys(name)
    driver.find_element_by_id(signup.signup_input_lastname_id).send_keys(lastName)
    driver.find_element_by_id(signup.signup_input_email_id).send_keys(email)
    driver.find_element_by_id(signup.signup_input_organization_id).send_keys(organization)
    driver.find_element_by_id(signup.signup_input_phone_id).send_keys(phone)
    driver.find_element_by_xpath(signup.signup_input_industry_xpath).click()
    driver.find_element_by_xpath(signup.signup_input_industry_xpath1).click()
    driver.find_element_by_xpath(signup.signup_slect_industryother_xpath).click()
    driver.find_element_by_id(signup.signup_input_password_id).send_keys(password)
    driver.find_element_by_id(signup.signup_input_confirmpassword_id).send_keys(confirmPassword)
    driver.find_element_by_id(signup.signup_button_submit_id).click()