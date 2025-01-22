# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Damien Xie
# djxie@uci.edu
# 63654608

from pathlib import Path
import shlex

def print_commands():
    print("""
Commands Available:
C - Create a new file in the specified directory.
D - Delete the file.
R - Read the contents of a file.
Q - Quit the program""")

def create_file(path):
    print(path)

# def delete_file():

# def read_file():

def explorer():
    command = ['']
    print_commands()

    while command[0].upper() != 'Q':
        command = input("\nWhat is your command?\n") #FIXME the command is not a single letter but a whole line
        command = shlex.split(command)
        if command[0].upper() == 'C':
            create_file(command[1:])
        # if command.upper() == 'D':
        #     delete_file()
        # if command.upper() == 'R':
        #     read_file()

if __name__ == "__main__":
    explorer()
    #test command C "/home/algol/ics32/lectures/l1/" -n student
                # D /home/algol/ics32/lectures/l1/student.dsu
                # R /home/algol/ics32/lectures/l1/student.dsu
