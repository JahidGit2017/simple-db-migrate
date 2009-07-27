from test import *
from helpers import *
from pmock import *
import unittest

class ListsTest(unittest.TestCase):
    
    def test_it_should_subtract_lists(self):
        a = ["a", "b", "c", "d", "e", "f"]
        b = ["a", "b", "c", "e"]
        result = Lists.subtract(a, b)
        
        self.assertEquals(len(result), 2)
        self.assertEquals(result[0], "d")
        self.assertEquals(result[1], "f")

    def test_it_should_subtract_lists2(self):
        a = ["a", "b", "c", "e"]
        b = ["a", "b", "c", "d", "e", "f"]
        
        result = Lists.subtract(a, b)

        self.assertEquals(len(result), 0)