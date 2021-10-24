#!/usr/bin/python3.9

from test_users_and_credentials import User
from test_users_and_credentials import Credential

def create_user(username,password):
    """Function to create a new user"""
    new_user = User(username,password)
    return new_user

def main():
    print("Hello! Welcome to SAFE PASSWORD VAULT.\nWhat is your name?")
    user = input().title()
    print("*"*80)
    print(f"\nHello {user}. Pick a short code to continue")
    print("\n")
    
    while True:
        print("use the exact short codes listed: ")
        print("-"*33)
        print("\n cu - Create new account")
        print("-"*33)

        
        short_code = input().lower().strip()
        if short_code == "cu":
            print("Enter preferred username: ")
            new_username = input().lower()
            print("Enter preferred password: ")
            new_password = input()
            print("Confirm new password: ")
            confirmed_password = input()
            while new_password!=confirmed_password:
                print("Passwords do not match")
                print("Enter preferred username: ")
                new_username = input().lower()
                print("Enter preferred password: ")
                new_password = input()
                print("Confirm new password: ")
                confirmed_password = input()
            else:
                create_user(new_username,new_password)
                print(f"\nNew account successfully created: \nUsername: {new_username} \nPassword: {new_password}\n")                
                print("*"*80)
                print("PROCEED TO LOGIN")
                print("*"*80,"\n")
        
        else:
            print("Kindly use the short codes provided")




            
        

    
if __name__ == '__main__':

    main()