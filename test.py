import sqlite3


with sqlite3.connect("my.db") as db:
    cursor = db.cursor()
    #cursor.execute("CREATE TABLE routes (id int, time int, target string);")
    #db.commit()
    selection = cursor.execute('''
        SELECT id FROM routes WHERE target in
            (SELECT id FROM stations WHERE y > 9)''')
    print(selection.fetchall())
