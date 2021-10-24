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
        
    def test_delete_user(self):
        """Test that confirms a user account and its credentials are deleted"""
        self.new_user.save_user()
        new_credential = Credential("twitter","goofy","0987")
        new_credential.save_credential()
        self.new_user.delete_user()
        self.assertEqual(len(User.users_list),0)
        self.assertEqual(len(Credential.credentials_list),0)
        
    def test_find_user(self):
        """Test that checks if a user and their 
        details can be found using the user's username"""
        self.new_user.save_user()
        found_user = User.find_user("minnie")
        self.assertEqual(self.new_user.password,found_user.password)
        
        
    def test_user_exists(self):
        """test to check if a Boolean is returned when a user is found."""
        self.new_user.save_user()
        confirmed_user = User.user_exists(self.new_user.username)
        self.assertTrue(confirmed_user)
class TestCredential(unittest.TestCase,):
    """Test class that defines the test cases for the Credential class"""
    
    def setUp(self):
        """setup method to run before each test case"""
        self.new_user = User("minnie","password")
        self.new_credential = Credential("twitter","goofy","0987")

        
    def tearDown(self):
        """tearDown method that does clean up after each test case has run"""
        Credential.credentials_list = []
    
    def test_credential_init(self):
        """Test to check whether the Credential object is being initialized properly """
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.c_username,"goofy")
        self.assertEqual(self.new_credential.c_password,"0987")
    
    def test_save_credential(self):
        """Test that confirms a credential is saved"""
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
        
    def test_save_multiple_credentials(self):        
        """Test that confirms multiple credentials are being saved"""
        self.new_credential.save_credential()
        second_credential = Credential("instagram","donald","5678")
        second_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def test_find_credential(self):
        """Test that checks if a user and their 
        details can be found using the user's username"""
        self.new_credential.save_credential()
        found_credential = Credential.find_credential("twitter","goofy")
        self.assertEqual(self.new_credential.c_password,found_credential.c_password)

        
        
    def test_display_credentials(self):
        """Test that confirms all a user's credentials are being displayed 
        by returning a list of saved credentials"""
        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)

        
    def test_delete_credential(self):        
        """Test that confirms that a credential account is properly deleted"""
        self.new_credential.save_credential()
        second_credential = Credential("instagram","donald","5678")
        second_credential.save_credential()
        third_credential = Credential("facebook","winnie","123456")
        third_credential.save_credential()
        self.new_credential.delete_credential()
        second_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list),1)



   
    
if __name__ == '__main__':
    unittest.main()