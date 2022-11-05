# This function adds two numbers
def add(x, y):
    return x+y

# This function subtracts two numbers
def subtract(x, y):
    return x-y


# This function multiplies two numbers
def multiply(x, y):
    return x*y

#Need to define divide function.
def divide (x,y):
    try:
        return x/y
    except ZeroDivisionError:
        print("You can't divide it by zero")
        return None