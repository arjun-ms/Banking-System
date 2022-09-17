#TODO
# Parent Class : User
# Holds details about an user
# Has function to show user details
# Child Class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposit, withdraw and view balance

# Parent Class
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print(f"""
                Personal Details
            -------------------------
                Name   : {self.name}
                Age    : {self.age}
                Gender : {self.gender}
                """)
        
# arjun = User('Arjun',20,'Male')
# print(arjun)
# arjun.show_details()