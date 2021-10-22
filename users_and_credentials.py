class User:
    """Class that generates new instances of users."""
    users_list = []
    
    def __init__(self,username,password):
        """Initialize username and password attributes"""
        
        self.username = username
        self.password = password
        
    def save_user(self):
        User.users_list.append(self)
    
    