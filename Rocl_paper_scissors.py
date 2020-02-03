# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 22:55:42 2020

@author: Yogesh Patel
"""

import random as rn #import random package and create alias name

user_selection = int(input("Please choose your hand motion : \n 1 : Rock \n 2 : Paper \n 3 : Scissors \n"))  #asks user to choose hand motion
computer_selection = int(rn.randint(1,4))  #system will choose random number within the given range
result_metric = [[0,-1,1],[1,0,-1],[-1,1,0]]  #define result metric to apply game rules
input_string = ["Rock","Paper","Scissors"]   #define list of hand motions to display input
result = result_metric[user_selection-1][computer_selection-1]

print("User selected: %s"%(input_string[user_selection-1]))
print("Computerized selected: %s \n"%(input_string[computer_selection-1]))

if result > 0:
    print("Great, You are a winner")
elif result == 0:
    print("It is a tie")
else:
    print("Unfortunately, You loose")