# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Damien Xie
# djxie@uci.edu
# 63654608

def calculate():
    print("Welcome to ICS 32 PyCalc!\n")

    operand1 = int(input("Enter your first operand: \n"))
    operand2 = int(input("Enter your second operand: \n"))
    operator = input("Enter your desired operator (+, -, or x): \n")

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "x":
        result = operand1 * operand2

    print(f"The result of your calculation is: {result}")

if __name__ == "__main__":
    calculate()