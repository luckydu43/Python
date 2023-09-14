from TodoDAOcontext import TodoDAOcontext

def completed_todos(generator_todos):
    for todo in generator_todos:
        if todo.completed :
            yield todo

def Etape21():
    print(50*'-')
    print ("test enter et exit")
    print(50*'-')
    with TodoDAOcontext(r"Partie4\todos_db.db") as dao:
        todos = list(dao.findAll())
        try: 
            raise InterruptedError("test pour voir la levée de l'exit malgré l'exception entre temps")
        
            # affiche le nombre d'items
            print (len(todos))
        except InterruptedError as erreurlevee:
            print (erreurlevee)
        
if __name__ == "__main__":
    Etape21()