'''
@Coded by TSG, 2021

Problem:


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
'''



#your code goes here
#Naive Solution
g,k=0,''
for i in (input().split()):
    if len(i) > g:
        g=len(i)
        k=i
print(k) 



# OR
# Try this:



print(max(input().split(), key=len))
