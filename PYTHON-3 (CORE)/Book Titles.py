'''
@Coded by TSG, 2021

Problem:


You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12
'''



file = open("/usercode/files/books.txt", "r")
#your code goes here
k= list(file)
for i in range(len(k)):
    if i!=len(k)-1:
        print(k[i][0]+str(len(k[i])-1))
    else:
        print(k[i][0]+str(len(k[i])))
file.close()


# OR      
# you can use this: (modifying the given statements)


for line in (open("/usercode/files/books.txt","r").readlines()): print(line[0] + str(len(line.rstrip("\n"))))        #removed "\n" from the list of strings!
