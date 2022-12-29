import re


class Register:
    def __init__(self, fname, lname, phonenumber, email, username, password):
        self.fname = fname
        self.lname = lname
        self.username = username
        if Register.phone_validator(phonenumber):
            self.phonenumber = phonenumber
        else:
            raise Exception("Invalid phonenumber!")
        if Register.email_validator(email):
            self.email = email
        else:
            raise Exception("Invalid email!")
        if self.pass_validator(password):
            self.password = password
        else:
            raise Exception("Invalid password!")

    @staticmethod
    def phone_validator(phonenumber):
        if re.match(r"\+98", phonenumber):
            return True
        else:
            return False

    @staticmethod
    def email_validator(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex, email):
            return True
        else:
            return False

    @staticmethod
    def pass_validator(password):
        regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
        if re.match(regex, password):
            return True
        else:
            return False


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
