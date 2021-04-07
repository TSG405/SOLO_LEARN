'''
@Coded by TSG, 2021

Problem:


You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
'''



#your code goes here
def concatenate(*args): return ('-'.join(args))
print(concatenate("I", "love", "Python", "!"))
