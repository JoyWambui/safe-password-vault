import unittest
from users_and_credentials import User

class TestUsers(unittest.TestCase):
    """Test class that defines the test cases for the user class"""
    
    def setUp(self):
        """setup method to run before each test case"""
        
        self.new_user = User("minnie","password")
        User.users_list = []
        
        
    def test_init(self):
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
  

if __name__ == '__main__':
    unittest.main()