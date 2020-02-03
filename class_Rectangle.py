# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:48:11 2020

@author: Yogesh Patel
"""

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def getArea(self):
        return self.length * self.width
    
    def getCircumference(self):
        return 2*(self.length + self.width)
    
c = Rectangle(5,3)
print("The area of rectangle is : ",c.getArea())
print("The area of rectangle is : ",c.getCircumference())