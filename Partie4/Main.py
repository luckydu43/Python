from TodoDAO import TodoDAO

def completed_todos(generator_todos):
    for todo in generator_todos:
        if todo.completed :
            yield todo

def Main():
    print(50*'-')
    print ("")
    print(50*'-')
    dao = TodoDAO(r"Partie4\todos_db.db")
    for todo in completed_todos(dao.findAll()):
        print(todo)
    ##for todo in todos :
    ##    print(todo)
	
if __name__ == "__main__":
    Main()