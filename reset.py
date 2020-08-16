#Resetting the datsbase to zero.
import sqlite3

#Carefully delete only when needed, this remove your whole database collected so far
# conn = sqlite3.connect('dump.sqlite')
# cur = conn.cursor()
#
# cur.executescript('''
# DROP TABLE IF EXISTS NAMEOFTABLE1;
# DROP TABLE IF EXISTS NAMEOFTABLE2;
# ''')
# conn.commit()
#
# cur.close()
# print("Dump data has been reset")

#Resets the ranks
conn = sqlite3.connect('sorted.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS NAMEOFTABLE1;
DROP TABLE IF EXISTS NAMEOFTABLE2;
''')
conn.commit()

cur.close()
print("Sorted data has been reset")
