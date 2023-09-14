import sqlite3

from Todo import Todo

class TodoDAOcontext:

    def __init__(self, fileSource):
        self._connection = sqlite3.connect(fileSource)
    
    def __enter__(self):
        print(f"enter (ça on s'y attend)")
        return self

    def __exit__(self, *exc):
        print(f"exit (ça on s'y attendait peut-être moins)")
        self._connection.close()

    def findAll(self):
        cursor = self._connection.cursor()
        result = cursor.execute("SELECT * FROM todos_table")
        ##todos=[]
        for id, title, completed in result.fetchall():
            yield Todo(id, title, completed)
            ##todos.append(Todo(id, title, completed))
        ##return todos

    def __del__(self):
        self._connection.close()