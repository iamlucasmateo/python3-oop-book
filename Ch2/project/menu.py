import sys
from note import Note
from notebook import Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
        Notebook Menu

        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid option")
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.content}")
    
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    def add_note(self):
        content = input("Note content: ")
        self.notebook.new_note(content)
        print("Your note has been added")
    
    def modify_note(self):
        id = input("Enter a note id: ")
        if not self.notebook.id_exists(id):
            print ("id does not exist")
            return
        new_content, new_tags = None, None
        modify_content = input("Modify content (Y/N)")
        if modify_content == "y":
            new_content = input("Note content: ")
            self.notebook.modify_note(id, new_content=new_content)
        modify_tags = input("Modify tags (Y/N)")
        if modify_tags == "y":
            new_tags = input("New tags: ")
            self.notebook.modify_note(id, new_tags=new_tags)
    
    def quit(self):
        print("Thank you")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()