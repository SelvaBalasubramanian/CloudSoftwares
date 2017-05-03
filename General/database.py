import sqlite3

db = sqlite3.connect(r"C:\Users\selva\PycharmProjects\CloudSoftwares\db.sqlite3")

print("sucess")

cursor = db.execute('SELECT * FROM General_Softwares')

for i in cursor:
	print (i[0])
	print (i[1])
	print (i[2])
	print ('\n')
