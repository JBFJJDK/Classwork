import sqlite3
 
name = input()
con = sqlite3.connect(name)
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT genre FROM Films
            WHERE year == 2010 or year == 2011""").fetchall()
 
for elem in result:
    print(elem[0])
 
con.close()