class User:
    """Class that models instances of users."""
    users_list = []
    
    def __init__(self,username,password):
        """Initialize username and password attributes"""
        
        self.username = username
        self.password = password
        self.credentials_list = Credential.credentials_list
        
    def save_user(self):
        """Saves created users to a predefined list"""

        User.users_list.append(self)
    
    def delete_user(self):
        """Deletes user accounts"""
        self.credentials_list.clear()
        User.users_list.remove(self)
    
        
    @classmethod
    def user_exists(cls,username):
        """Method that checks whether a user account exists"""
        for user in cls.users_list:
            if user.username == username:
                return True
        return False
        
    
        
class Credential():
    """Class that instantiates new credentials that 
    requires an account name, username and password"""
    credentials_list = []
    
    def __init__(self,account_name,username,password):
        """Initialize account_name, username, and password attributes"""
        
        self.account_name = account_name
        self.username = username
        self.password = password
        
    def save_credential(self):
        """Saves created credentials to a predefined list in the user class"""

        Credential.credentials_list.append(self)
        
    def delete_credential(self):
        """Deletes credential accounts"""
        Credential.credentials_list.remove(self)
    
    @classmethod    
    def display_credentials(cls):
        """Displays all of a user's saved credentials"""
        return cls.credentials_list




 

    