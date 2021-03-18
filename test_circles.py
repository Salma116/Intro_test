import unittest
from circles import circle_area
from math import pi

class TestCircleArea (unittest.TestCase): 
    def test_area(self): #each test methods must start with the word test 
        #test areas when rad>=0
        self.assertAlmostEqual(circle_area(1), pi) #output of the circle area function, correct answer if these two are correct test pass. 
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*2.1**2) 
    # def test_values(self):
    #     self.assertRaises (ValueError, circle_area, -2)
    #     #lancer le test = python -m unittest filename