'''
@Coded by TSG, 2021

Problem:


You are given a Juice class, which has name and capacity properties.
You need to complete the code to enable and adding of two Juice objects, resulting in a new Juice object with the combined capacity and names of the two juices being added.

For example, if you add an Orange juice with 1.0 capacity and an Apple juice with 2.5 capacity, the resulting juice should have:
name: Orange&Apple
capacity: 3.5

The names have been combined using an & symbol.
'''



#your code goes here
class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    def __add__(self,other):
        return(self.name+'&'+other.name+' '+'('+str(self.capacity + other.capacity)+'L)')
    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)
result = a + b
print(result)
