#!/usr/bin/python3.9

from test_users_and_credentials import User
from test_users_and_credentials import Credential
import random
import string

def creates_user(username,password):
    """Function to create a new user"""
    new_user = User(username,password)
    return new_user

def saves_user(user):
    """Function to save a new user"""
    user.save_user()
    
def finds_user(username):
    """Function that finds a user account and returns it."""
    return User.find_user(username)
    
def confirm_user_exists(username):
    """Function that checks whether a user account exists and returns a Boolean"""
    return User.user_exists(username)

def creates_credential(account_name,c_username,c_password):
    """Function to add a credential"""
    new_credential = Credential(account_name,c_username,c_password)
    return new_credential

def saves_credential(credential):
    """Function that saves added credentials."""
    credential.save_credential()

def generate_password(password_length):
    """Function that auto-generates a mixed character password of a desired length""" 
    possible_characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = "".join(random.choice(possible_characters) for i in range(password_length))
    return generated_password
        
def main():
    print("Hello! Welcome to SAFE PASSWORD VAULT.\nWhat is your name?")
    user = input().title()
    print("*"*80)
    print(f"\nHello {user}. Pick a short code to continue")
    print("\n")
    
    while True:
        print("\nUse the exact short codes listed: ")
        print("-"*33)
        print("\n cu - Create new account \n lg - Login to account")
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
                print("_"*80)
                print("Passwords do not match")
                print("_"*80)
                print("\nEnter preferred username: ")
                new_username = input().lower()
                print("Enter preferred password: ")
                new_password = input()
                print("Confirm new password: ")
                confirmed_password = input()
            else:
                saves_user(creates_user(new_username,new_password))
                print(f"\nNew account successfully created: \nUsername: {new_username} \nPassword: {new_password}\n")                
                print("*"*80)
                print("PROCEED TO LOGIN")
                print("*"*80,"\n")
        
        elif short_code == "lg":
            print("Enter username: ")
            login_username = input().lower()
            print("\nEnter password: ")
            login_password = input()
            if confirm_user_exists(login_username) == False:
                print("_"*80)
                print("The user does not exist. Create an account.")
                print("_"*80)
            else:
                found_username = finds_user(login_username)
                while login_password != found_username.password:
                    print("\n")
                    print("_"*80)
                    print("Wrong password. Input the correct password")
                    print("_"*80,"\n")
                    print("Enter username: ")
                    login_username = input().lower()
                    print("\nEnter password: ")
                    login_password = input()
                else:
                    while True:
                        print("\n")
                        print("*"*80)
                        print("LOGIN SUCCESSFUL!!!")
                        print("*"*80,"\n")
                        print("use the exact short codes listed for credentials: ")
                        print("+"*45)
                        print("\n ac - Add existing credential \n nc - Create new credential")
                        print("+"*45,"\n")
                        credential_short_code = input().lower().strip()
                        
                        if credential_short_code == "ac":
                            print("\nEnter Account Name: ")
                            existing_account_name = input().title()
                            print("\nEnter Account Username: ")
                            existing_account_username = input()
                            print("\nEnter Account Password: ")
                            existing_account_password = input()
                            saves_credential(creates_credential(existing_account_name,existing_account_username,existing_account_password))
                            print(f"\nNew credential successfully added: \nAccount Name: {existing_account_name} \nAccount Username: {existing_account_username} \nAccount Password: {existing_account_password}\n")                
                            print("use the exact short codes listed for credentials: ")
                            print("+"*45)
                            print("\n ac - Add existing credential \n nc - Create new credential")
                            print("+"*45,"\n")
                            
                        elif credential_short_code == "nc":
                            print("\nEnter Account Name: ")
                            new_account_name = input().title()
                            print("\nEnter Account Username: ")
                            new_account_username = input()
                            print("\nWould you like an autogenerated password?  Y/N")
                            answer = input().upper()
                            while answer != "Y" and answer != "N":
                                print("_"*80)
                                print("Pick from the given choices Y/N")
                                print("_"*80)
                                print("\nWould you like an autogenerated password?  Y/N")
                                answer = input().upper()
                            else:
                                if answer == "Y":
                                    print("\nEnter length of password: (0~9)")
                                    string_password_length = input()
                                    while string_password_length.isdecimal() == False:
                                        print("\n")
                                        print("_"*80)
                                        print("Input a number in the form (0,1,2,...,10,...)")
                                        print("_"*80,"\n")
                                        print("\nEnter length of password: (0~9)")
                                        string_password_length = input()
                                    else:
                                        password_length = int(string_password_length)
                                        generated_password = generate_password(password_length)
                                        saves_credential(creates_credential(new_account_name,new_account_username,generated_password))
                                        print(f"\nNew credential successfully created: \nAccount Name: {new_account_name} \nAccount Username: {new_account_username} \nAccount Password: {generated_password}\n")                
                                        print("use the exact short codes listed for credentials: ")
                                        print("+"*45)
                                        print("\n ac - Add existing credential \n nc - Create new credential")
                                        print("+"*45,"\n")
                                elif answer == "N":
                                    print("\nEnter Preferred Account Password: ")
                                    new_account_password = input()
                                    saves_credential(creates_credential(new_account_name,new_account_username,new_account_password))
                                    print(f"\nNew credential successfully created: \nAccount Name: {new_account_name} \nAccount Username: {new_account_username} \nAccount Password: {new_account_password}\n")                
                                    print("use the exact short codes listed for credentials: ")
                                    print("+"*45)
                                    print("\n ac - Add existing credential \n nc - Create new credential")
                                    print("+"*45,"\n")
                        else:
                            print("Kindly use the credential short codes provided")
      
        else:
            print("Kindly use the short codes provided")

    
if __name__ == '__main__':

    main()