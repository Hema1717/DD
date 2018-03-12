import json
def get_default_register_credentials():
    fpath = "C:/Users/Hema/DD/dd/config/master_testbed.json"

    with open(fpath) as f_json_data:
        testbed_file = json.load(f_json_data)
        f_json_data.close()
    print (testbed_file)

    default_register_credentials_key = testbed_file['default_register_credentials']
    print(default_register_credentials_key)

    firstName = default_register_credentials_key['register_fname']
    register_lname = default_register_credentials_key['register_lname']
    register_email = default_register_credentials_key['register_email']
    register_companyname = default_register_credentials_key['register_companyname']
    register_phone = default_register_credentials_key['register_phone']
    register_password = default_register_credentials_key['register_password']
    register_confirmpassword = default_register_credentials_key['register_confirmpassword']



    return firstName,register_lname, register_email,register_companyname,register_phone,register_password, register_confirmpassword