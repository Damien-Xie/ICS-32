#lab3.py

# Starter code for lab 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Damien
# djxie@uci.edu
# 63654608

def readfile():
    with open("pynote.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line)


def writenote():
    noquit = True
    with open("pynote.txt", 'a') as file:
        while noquit:
            note = input("Please enter a new note (enter q to exit):")
            if note != "q":
                file.write(note + "\n")
            else:
                noquit = False


def pynote():
    print("Welcome to PyNote!")
    print("Here are your notes:\n")

    readfile()
    writenote()




if __name__ == "__main__":
    pynote()

