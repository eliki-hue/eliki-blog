import unittest
from app.models import User


User=User

class UserTest(unittest.TestCase):
     '''
    Test Class to test the behaviour of the Channel class
    '''

     def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User('john', 'john@gmail.com',111111)
     def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))


if __name__ == '__main__':
    unittest.main()