import sqlite3

from Todo import Todo

class TodoDAO:

    def __init__(self, fileSource):
        self._connection = sqlite3.connect(fileSource)

    def findAll(self):
        cursor = self._connection.cursor()
        result = cursor.execute("SELECT * FROM todos_table")
        for id, title, completed in result.fetchall():
            t = Todo(id, title, completed)
            print(t)

    def __del__(self):
        self._connection.close()