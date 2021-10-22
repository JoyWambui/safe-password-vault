import unittest
from users_and_credentials import User
from users_and_credentials import Credential

class TestUser(unittest.TestCase):
    """Test class that defines the test cases for the user class"""
    
    def setUp(self):
        """setup method to run before each test case"""
        
        self.new_user = User("minnie","password")
    def tearDown(self):
        """tearDown method that does clean up after each test case has run"""
        User.users_list = []
        
        
    def test_user_init(self):
        """Test to check whether the User object is being initialized properly """
        self.assertEqual(self.new_user.username,"minnie")
        self.assertEqual(self.new_user.password,"password")
        
    def test_save_user(self):
        """Test that confirms a user account is being saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)
        
    def test_save_multiple_users(self):        
        """Test that confirms multiple user accounts are being saved"""
        self.new_user.save_user()
        second_user = User("micky","1234")
        second_user.save_user()
        self.assertEqual(len(User.users_list),2)
        
class TestCredential(unittest.TestCase):
    """Test class that defines the test cases for the Credential class"""
    
    def setUp(self):
        """setup method to run before each test case"""
        
        self.new_credential = Credential("twitter","goofy","0987")
        
    def test_credential_init(self):
        """Test to check whether the Credential object is being initialized properly """
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.username,"goofy")
        self.assertEqual(self.new_credential.password,"0987")
    
   
    
  

if __name__ == '__main__':
    unittest.main()