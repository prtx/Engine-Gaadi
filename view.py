import sqlite3
conn = sqlite3.connect('Data.db')
conn.text_factory = str
db = conn.cursor()

data = db.execute('select * from DATA')
for a_line in data:
    print a_line[0]
    print a_line[1]
    print a_line[2]
    print a_line[3]
    print a_line[4]
    print '\n'

conn.close()
