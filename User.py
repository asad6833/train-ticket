class User:

    def __init__(self, username, password, email, name, phone_number, credit_card_number,credit_card_expiry):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.phone_number = phone_number
        self.credit_card_number = credit_card_number
        self.credit_card_expiry = credit_card_expiry
    
    def get_username(self):
        return self.username
        
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_phone_number(self):
        return self.phone_number
    
    def get_address(self):
        return self.address
    
    def get_credit_card_number(self):
        return self.credit_card_number
    
    def get_credit_card_expiry(self):
        return self.credit_card_expiry

    def set_name(self, name):
        self.name = name
    
    def set_email(self, email):
        self.email = email
    
    def set_password(self, password):
        self.password = password

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def set_address(self, address):
        self.address = address
    
    def set_credit_card_number(self, credit_card_number):
        self.credit_card_number = credit_card_number
    
    def set_credit_card_expiry(self, credit_card_expiry):
        self.credit_card_expiry = credit_card_expiry

    def set_username(self, username):
        self.username = username

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number,
            "credit_card_number": self.credit_card_number,
            "credit_card_expiry": self.credit_card_expiry
        }
