"""
You already know how to convert a string into a number using the int() and float() functions.

This type of conversion is not a one-way street. You can also convert a number into a string, which is way easier and safer
This kind of operation is always possible.

A function capable of doing that is called str():

str(number)

It can do much more than transform numbers into strings, but that can wait for later.

Here is our "right-angle triangle" program again:
"""

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

"""
We've modified it a bit to show you how the str() function works.
Thanks to this, we can pass the whole result to the print() function as one string, forgetting about the commas.


You've made some serious strides on your way to Python programming.

You already know the basic data types and a set of fundamental operators.
You know how to organize the output and how to get data from the user. These are very strong foundations for Module 3.
But before we move on to the next module, let's do a few labs, and recap all that you've learned in this section.
"""
