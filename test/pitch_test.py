import unittest
from ..app import models

Pitch = models.Pitch


class PitchTest(unittest.TestCase):
     '''
    Test Class to test the behaviour of the Pitch class
    '''

     def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch('john', 'john@gmail.com',1111)
     def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()