from TodoDAO import TodoDAO

def Main():
    print(50*'-')
    print ("")
    print(50*'-')
    dao = TodoDAO(r"Partie4\todos_db.db")
    dao.findAll()
	
if __name__ == "__main__":
    Main()