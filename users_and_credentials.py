class User:
    """Class that models instances of users."""
    users_list = []
    
    def __init__(self,username,password):
        """Initialize username and password attributes"""
        
        self.username = username
        self.password = password
        
    def save_user(self):
        """Saves created users to a predefined list"""

        User.users_list.append(self)
        
class Credential:
    """Class that instantiates new credentials that 
    requires an account name, username and password"""
    
    def __init__(self,account_name,username,password):
        """Initialize account_name, username, and password attributes"""
        
        self.account_name = account_name
        self.username = username
        self.password = password
 

    