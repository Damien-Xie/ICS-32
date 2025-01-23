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

def test_create(command):
    assert len(command) == 4
    path = Path(command[1])
    assert path.exists()
    name = command[3] + ".dsu"
    path = path / name
    assert not path.exists()
    assert command[2] == '-n'
    
def test_delete(command):
    assert len(command) == 2
    path = Path(command[1])
    assert path.exists()
    assert command[1][-4:] == ".dsu"

def test_read(command):
    assert len(command) == 2
    path = Path(command[1])
    assert path.exists()
    assert command[1][-4:] == ".dsu"

def create_file(command):
    test_create(command)
    name = command[3] + ".dsu"
    path = Path(command[1]) / name

    if not path.exists():
        path.touch(exist_ok=True)
    print(path)

def delete_file(command):
    test_delete(command)
    path = Path(command[1])
    path.unlink()

    print(command [1] + " DELETED")

def read_file(command):
    test_read(command)
    path = Path(command[1])

    file = path.open('r')
    lines = file.readlines()
    if lines == []:
        print("EMPTY")
    else:
        for line in lines:
            print(line, end='')
    file.close()

def explorer():
    print_commands()

    try:
        command = input("\nWhat is your command?\n") #"\nWhat is your command?\n"
        if command == 'Q':
            return
        
        command = shlex.split(command)

        if command[0] == 'C':
            create_file(command)
        elif command[0] == 'D':
            delete_file(command)
        elif command[0] == 'R':
            read_file(command)
    except AssertionError:
        print("ERROR")

    explorer()

if __name__ == "__main__":
    explorer()
    #test command C "c:\Users\daXie\ICS 32" -n student
                # D "c:\Users\daXie\ICS 32/student.dsu"
                # R "c:\Users\daXie\ICS 32/student.dsu"
