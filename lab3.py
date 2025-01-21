#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Damien
# djxie@uci.edu
# 63654608

from pathlib import Path

def readfile(path):
    file = path.open('r')
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()


def writenote(path):
    file = path.open('a')
    noquit = True
    while noquit:
        note = input("Please enter a new note (enter q to exit):")
        if note != "q":
            file.write(note + "\n")
        else:
            noquit = False
    file.close


def createfile(path):
    file = path.open('x')
    file.close()

def pynote():
    path = Path("./pynote.txt")
    if not path.exists():
        createfile(path)

    print("Welcome to PyNote!")
    print("Here are your notes:\n")

    readfile(path)
    writenote(path)

if __name__ == "__main__":
    pynote()

