import unittest
from users_and_credentials import User

class TestUsers(unittest.TestCase):
    """Test class that defines the test cases for the user class"""
    
    def setUp(self):
        """setup method to run before each test case"""
        
        self.new_user = User("minnie","password")
        
    def test_init(self):
        """Test to check whether the User object is being initialzed properly """
        self.assertEqual(self.new_user.username,"minnie")
        self.assertEqual(self.new_user.password,"password")
if __name__ == '__main__':
    unittest.main()