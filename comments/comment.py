# This is an example of a comment. A remark inserted into a program, which is omitted at runtime is called a comment.
# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of square root.
print("c =", c)

# Good, responsible developers describe each vital piece of code, e.g., explaining the role of the variables.
# However, it must be stated that the best way to comment on variables is to name them unambiguously.

# Comments may be useful in another respect - you can use them to mark a piece of code that currently isn't needed for whatever reason.
#  Look at the example below, if you uncomment the highlighted line, this will affect the output of the code:
# This is a test program.
x = 1
y = 2
# y = y + x
print(x + y)

# This is often done during the testing of a program, to isolate the place where an error might be hidden.
# TIP: If you'd like to quickly comment or uncomment multiple lines of code, select the line(s) you wish to modify and use the following...
# keyboard shortcut: CTRL + / (Windows) or CMD + / (Mac OS). It's a very useful trick, isn't it? Try this code in Sandbox.

#uncomment_me = 1
#uncomment_me_too = 3
#uncomment_me_also = 5

print(uncomment_me, uncomment_me_too, uncomment_me_also, sep="\n")

