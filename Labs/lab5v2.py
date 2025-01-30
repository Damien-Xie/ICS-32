#lab5.py

# Starter code for lab 5 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Damien Xie
# djxie@uci.edu
# 63654608

# ---------------------

# Write your Note class here

class Note:
    def __init__(self, path):
        self.path = path
        
    def save_note(self, note):
        pynote = self.path.open('a')
        pynote.write(note + '\n')
        pynote.close()

    def read_notes(self):
        pynote = self.path.open('r')
        notes = pynote.readlines()
        pynote.close()

        return notes

    def remove_note(self, id):
        pynote = self.path.open('r')
        notes = pynote.readlines()
        remove_note = notes[id]
        notes.pop(id)

        pynote = self.path.open('w')
        for line in notes:
            pynote.write(line)

        pynote.close()

        return remove_note

# ---------------------
from pathlib import Path

NOTES_PATH = "."
NOTES_FILE = "pynote.txt"

def print_notes(notes:list[str]):
    id = 0
    for n in notes:
        print(f"{id}: {n}")
        id+=1

def delete_note(note:Note):
    try:
        remove_id = input("Enter the number of the note you would like to remove: ")
        remove_note = note.remove_note(int(remove_id))
        print(f"The following note has been removed: \n\n {remove_note}")
    except FileNotFoundError:
        print("The PyNote.txt file no longer exists")
    except ValueError:
        print("The value you have entered is not a valid integer")

def run():
    p = Path(NOTES_PATH) / NOTES_FILE
    if not p.exists():
        p.touch()
    note = Note(p)
    
    print("Here are your notes: \n")
    print_notes(note.read_notes())

    user_input = input("Please enter a note (enter :d to delete a note or :q to exit):  ")

    if user_input == ":d":
        delete_note(note)
    elif user_input == ":q":
        return
    else:    
        note.save_note(user_input)
    run()


if __name__ == "__main__":
    print("Welcome to PyNote! \n")

    run()
