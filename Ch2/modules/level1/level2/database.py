class Database:
    pass

database = None

def init_db():
    global database
    database = Database()
    return database