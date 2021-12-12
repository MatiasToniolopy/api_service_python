import sqlite3 as sql
import matplotlib.pyplot as plt

conn = sql.connect('personas.db')
c = conn.cursor()

data = c.execute('SELECT * FROM persona')

age = [x[2] for x in data]


data2 = c.execute('SELECT * FROM persona')

ritmo = [x[3] for x in data2]


plt.figure()
plt.subplot()
c = ['red','blue','green','yellow','orange', 'purple']
plt.bar(age, ritmo, width=9.5, color=c)
plt.title('RITMO CARDIACO BASADO EN EDADES', color='red')
plt.xlabel('EDAD', color='green')
plt.ylabel('RITMO CARDIACO', color='blue')
plt.grid()
plt.show()



