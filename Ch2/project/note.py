from datetime import datetime

class Note:
    id = 0
    def __init__(self, content, tags=""):
        self.content = content
        self.tags = tags
        self.id = Note.id
        Note.id += 1
        self.creation_date = datetime.now()
