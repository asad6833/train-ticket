import User
import TicketController
import Station
import Station_Controller
from TicketController import Ticket
from User_Controller import User_Controller

class UserInterface:
    
    def __init__(self, user_controller):
        self.user_controller = user_controller
        self.station_controller = Station_Controller
        self.user = None
        self.ticket = None
        self.station = None
    
    def start_screen(self):
        print("1. Existing Member Login")
        print("2. New Member Registration")

        selection = input("Select an option to either login or register.")

        if selection == "1":
            self.display_login()
        elif selection == "2":
            self.display_registration()
        else:
            print("Invalid Selection. Please Retry.")

    def display_login(self):
        username = input("Username: ")
        password = input("Password: ")
        self.user_controller.load_users()
        if self.user_controller.login(username, password):
            print("Login Successful! ")
            self.user = self.user_controller.get_user_by_username(username)
            print(f"Welcome Back {self.user.name} ! ")
            self.display_home()
        else:
            print("Invalid username or password")
            self.start_screen()

    def display_registration(self):
        print("Please enter your details to register")
        username = input("Username: ")
        password = input("Password: ")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        credit_card_number = input("Credit Card Number: ")
        credit_card_expiry = input("Credit Card Expiry: ")
        if self.user_controller.register_user(username, password, name, email, phone, credit_card_number, credit_card_expiry):
            print("You are now registered. Please log in.")
            self.display_login()
        else:
            print("Username is already taken. ")
        
    def display_home(self):
        print("1. Book Ticket ")
        print("2. Manage Tickets ")
        print("3. View Train Schedule ")
        print("4. Manage Profile ")

        selection = input("Select an option to view the window ")
        
        if selection == "1":
            self.display_ticket_booking()
        elif selection == "2":
            self.display_manage_tickets()
        elif selection == "3":
            self.display_train_schedule()
        elif selection == "4":
            self.display_profile()
    
    def display_ticket_booking(self):
        #Need to implement the actual ticket booking through the ticket controller
        print(f"Congratulations!  {self.user.name} your ticket has been booked")
    
    def display_manage_tickets(self):
        print("1. Cancel Ticket")
        print("2. Get Ticket Details")
        print("3. Back to main page")

        selection = input("Select an option. ")

        if selection == "1":
            return
            #Run Cancel Ticket Method
        elif selection == "2":
            return
            #Run Get Ticket Method
        elif selection == "3":
            self.display_home()
        else:
            print("Invalid Selection")
            
    
    def display_train_schedule(self):
        return

    def display_profile(self):
        print(f"1. Username: {self.user.username} ")
        print(f"2. Email: {self.user.email} ")
        print(f"3. Password: {self.user.password} ")
        print("4. <- Back ")

        selection = input("Select an option to edit or select 4 to go back to the main page.")

        if selection == "4":
            self.display_home()
        else:
            self.edit_selection(selection)

    def edit_selection(self, selection):
        if selection == "1":
            new_name = input("Enter new name: ")
            self.user.set_username(new_name)
            print("New name has been set")
        elif selection == "2":
            new_email = input("Enter new email: ")
            self.user.set_email(new_email)
            print("New email has been set")
        elif selection == "3":
            new_password = input("Enter new password: ")
            self.user.set_password(new_password)
            print("New name has been set")
        else:
            print("Invalid selection")
            self.display_profile()
            return

uc = User_Controller()
ui = UserInterface(uc)

#Start Screen Test
ui.start_screen()

#Register New User
#ui.display_registration()

#Existing User Login
#ui.display_login()
