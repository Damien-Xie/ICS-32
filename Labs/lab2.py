#lab2.py

# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Damien Xie
# djxie@uci.edu
# 63654608

def add(a, b):
    return  a + b

def sub(a, b):
    return  a - b

def div(a, b):
    try:
        return  a / b
    except ZeroDivisionError:
        return "Can't divide by zero"

def mul(a, b):
    return  a * b

def run():
    try:
        a = float(input("Enter left operand: "))
        b = float(input("Enter right operand: "))
        operator = input("What type of calculation would you like to perform (+, -, x, /)? ")
                
        r = 0

        if operator == "+":
            r = add(a,b)
        elif operator == "-":
            r = sub(a,b)
        elif operator == "x":
            r = mul(a,b)
        elif operator == "/":
            r = div(a,b)
        else:
            r = "Unable to perform the desired calculation, please try again."

        print(r)

    except ValueError:
        print("Invalid operand")    
    
    
    if input("Run another calculation (y/n)? ") == "y":
        run()


if __name__ == "__main__":
    print("Welcome to PyCalc!")
    run()
