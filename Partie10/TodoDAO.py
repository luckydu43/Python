import sqlite3

from EntityTodo import Todo

class TodoDAO:

    def __init__(self, fileSource):
        self._connection = sqlite3.connect(fileSource)

    def findAll(self):
        cursor = self._connection.cursor()
        result = cursor.execute("SELECT * FROM todos_table")
        ##todos=[]
        for id, title, completed in result.fetchall():
            yield Todo(id, title, completed)
            ##todos.append(Todo(id, title, completed))
        ##return todos

    def delete(self, id):
        cursor = self._connection.cursor()
        cursor.execute(f"DELETE FROM todos_table WHERE id ={id}")
        self._connection.commit()
       
    def __del__(self):
        self._connection.close()