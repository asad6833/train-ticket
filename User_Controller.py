from User import User
import json

class User_Controller:
    def __init__(self):
        self.user_list = []
        self.file_path = "users.json"
        
    def register_user(self, username, password, name, email, phone, credit_card_number, credit_card_expiry):
        for user in self.user_list:
            if user.username == username:
                return False
        self.user_list.append(User(username, password, name, email, phone, credit_card_number, credit_card_expiry))
        self.convert_to_json()
        return True
    
    
    def login(self, username, password):
        self.load_users()
        for user in self.user_list:
            if user.username == username and user.password == password:
                return True
        return False
    
    def logout(self, user_id):
        # assuming user_id is the index of the user in the user_list
        if user_id < len(self.user_list):
            # perform logout action here
            return
        raise ValueError("Invalid user id")
    
    def update_user_details(self, user_id, name, email, phone, credit_card_number, credit_card_expiry):
        if user_id < len(self.user_list):
            user = self.user_list[user_id]
            user.name = name
            user.email = email
            user.phone = phone
            user.credit_card_number = credit_card_number
            user.credit_card_expiry = credit_card_expiry
            return True
        return False

    def get_user_by_username(self, username):
        for user in self.user_list:
            if user.username == username:
                return user
        return None
    
    def convert_to_json(self):
        json_dict = [user.to_dict() for user in self.user_list]
        with open("users.json","w") as f:
            json.dump(json_dict,f)

    def load_users(self):
        try:
            with open(self.file_path, "r") as f:
                users = json.load(f)
                self.user_list = [User(**user) for user in users]
        except FileNotFoundError:
            pass
