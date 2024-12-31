import sqlite3, random

# ouverture/initialisation de la base de donnee 
conn = sqlite3.connect('bibli.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

# affichage d'une table
# lecture dans la base avec un select
c.execute('SELECT * FROM Etudiant')

# parcourt ligne a ligne
for raw in c.execute('SELECT * FROM Etudiant'):
	print raw.keys()
	print raw["Nom"]

# insertion d'une donnee
c.execute("INSERT INTO Emprunte VALUES (4,1,'23/10/2020')")

# insertion de plusieurs donnees
values = []
for i in range(3):
	values.append((random.randint(1,5),i+1,"'%d/11/2020'" %(random.randint(1,30))))
c.executemany('INSERT INTO Emprunte VALUES (?,?,?)', values)

# lecture dans la base avec un select
c.execute('SELECT * FROM Emprunte')
#print c
#print c[0]
print c.fetchall()

# fermeture
conn.commit()
conn.close()
