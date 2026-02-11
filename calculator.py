x = input("What's x? ")
y = input("What's y? ")

# "int" is actually a function the gets the integer value(if there is one) of the selected variable and outputs that.
# z = int(x) + int(y)
# the "round" function rounds the number to the nearest integer
z = round(float(x) + float(y))

print(z)
