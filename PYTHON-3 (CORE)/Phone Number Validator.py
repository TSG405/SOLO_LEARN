'''
@Coded by TSG, 2021

Problem:


You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
'''



#your code goes here
# Without using Regex module:
g =list(input())
if(len(g))==8:
    if (g[0]=='1' or g[0]=='8'or g[0]=='9'): print("Valid")
    else: print("Invalid")
else: print("Invalid")
  
# OR
# Using Regex module:
def isValid(s):
    Pattern = re.compile("[189]\d{7}$")
    return Pattern.match(s) 
if (isValid(input())): print ("Valid")     
else: print ("Invalid")
