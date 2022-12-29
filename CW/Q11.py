import re


class Register:
    users_dict={}
    def __init__(self,fname,lname,phonenumber,email,username,password):

        self.fname=fname
        self.lname=lname
        if Register.phone_validator(phonenumber):
            self.phonenumber=phonenumber
        else:
            raise Exception ("Invalid phonenumber!")
        if Register.email_validator(email):
            self.email=email
        else:
            raise Exception("Invalid email!")
        self.username=username
        if Register.pass_validator(password):
            self.password=password
        else:
            raise Exception("Invalid password!")

        self.users_dict.setdefault(self.username,self.password)


    @staticmethod
    def phone_validator(phonenumber):
        if re.match(r"\+98",phonenumber):
            return True
        else:
            return False
    @staticmethod
    def email_validator(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex,email):
            return True
        else:
            return False
    @staticmethod
    def pass_validator(password):
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
        if re.match(regex,password):
            return True
        else:
            return False

class Login:
    @staticmethod
    def login(username,password):
        if username in Register.users_dict and password==Register.users_dict[username]:
            return True
        else:
            return False

while True:
    user_decision=input("Enter 1 (for register) or 2 (for login) or 0 (exit)--->")
    if user_decision=="1":
        user_fname=input("Enter first name--->")
        user_lname = input("Enter last name--->")
        user_phone = input("Enter phonenumber--->")
        user_email = input("Enter email--->")
        user_username = input("Enter username--->")
        user_password= input("Enter password--->")
        register_obj=Register(user_fname,user_lname,user_phone,user_email,user_username,user_password)

    elif user_decision=="2":
        user_username=input("Enter username--->")
        user_password=input("Enter password--->")
        print(Login.login(user_username,user_password))

    elif user_decision=="0":
        exit()

    else:
        print("Wrong decision!!!")