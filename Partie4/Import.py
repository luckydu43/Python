
import csv
import sqlite3


def Import():

    print(50*'-')
    print ("Importation d'un CSV dans une BDD SQLite")
    print(50*'-')

    connection = sqlite3.connect(r"Partie4\todos_db.db")
    cursor = connection.cursor()

    with open("Partie4\MOCK_DATA.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            row['completed'] = True if row['completed'] == 'true' else False
            ##sql = f"""INSERT INTO todos_table(title, completed)
            ##        VALUES('{row['title']}',{row ['completed']})"""
            sql = "INSERT INTO todos_table(title, completed) VALUES('{title}',{completed})".format(**row)
            print (sql)
            cursor.execute(sql)        
    connection.commit()
    result = cursor.execute("SELECT title FROM todos_table")
    print(result.fetchall())
    sql = r"DELETE FROM todos_table WHERE title LIKE '%title%'"
    print (sql)
    cursor.execute(sql)
    connection.commit()
    connection.close()

if __name__ == "__main__":
    Import()