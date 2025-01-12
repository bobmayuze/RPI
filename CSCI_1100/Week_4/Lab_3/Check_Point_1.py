# Author: Yuze Ma
# Date: Sept, 19th, 2016
# This code is made for Lab 3, Checkpoint 1

"""
This program experiments with the use of functions
and also learning error checking.


"""
# Import math module to actvate the function
import math

## Function returns the length of a line 
## starting at (x1,y1) and ending at (x2,y2)
def line_length(x1,y1,x2,y2):
    length = (x1-x2)**2 + (y1-y2)**2
    length = math.sqrt(length)
    return length

# Initialize all variables needed and input variables
initial_x = 10
initial_y = 10
next_x = float(input("The next x value ==> "))
next_y = float(input("The next y value ==> "))
total_length = line_length(initial_x, initial_y, next_x, next_y)


# output the resulets
print("The line has moved from ({0:d},{1:d}) ".format(initial_x, initial_y),"to (", next_x, ",", next_y,")", sep = '')
print("Total length traveled is",round(total_length))
