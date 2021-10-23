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



 

    