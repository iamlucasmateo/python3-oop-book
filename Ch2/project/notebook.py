from note import Note

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, content, tags=""):
        note = Note(content, tags)
        self.notes.append(note)
    
    def modify_note(self, note_id, new_content=None, new_tags=None):
        if self.id_exists(note_id):
            for note in self.notes:
                if str(note.id) == str(note_id):
                    if new_content:
                        note.content = new_content
                    if new_tags:
                        note.tags = new_tags
                    modified = True
                    break
        else:
            raise NoteNotFoundError(f"There is no note with id {note_id}")
    
    def id_exists(self, note_id):
        for note in self.notes:
            if str(note.id) == str(note_id):
                return True
        return False

    
    def search(self, filter:str):
        filtered_notes = []
        for note in self.notes:
            if filter in note.content or filter in note.tags:
                filtered_notes.append(note)
        return filtered_notes


class NoteNotFoundError(Exception):
    pass



    