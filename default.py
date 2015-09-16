# Default shell for a Python 3.x program
# Copy this and rename it to write your own code
#
__author__ = 'Nathaniel'

# Your class
# Name of program
#
# Brief description of what program does.

# Declare Magic Numbers and Constants

# LOOPCOUNTER = 2
# name = "Nathan"

# Write program code here


# Output
# First Assignment

for i in range(0,101,10):
    x = i * (9/5) + 32
    print(i,x)
    
# Second Assignment
F = eval(input("please input a temperature in Fahrenheit:"))
C = (F-32) * (5/9)
print("The temp",F, " is equal to",C, " Celsius")

# Third Assignment
K = eval(input("Please input a distance in kilometers"))
M = K * 0.62
print(K," kilometers is equal to ", M, " in miles.")
