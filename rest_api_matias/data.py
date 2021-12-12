import sqlite3 as sql

def createdb():
    
    conn = sql.connect('personas.db')
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE persona (
        [id] integer primary key,
        [nombre] text,
        [edad] integer,
        [r_c] integer
    );
    """)
    
    conn.commit()
    conn.close()
    
def agregar():
    conn = sql.connect('personas.db')
    cursor = conn.cursor()
    data = [
        ('matias', 34, 90),
        ('mariela', 22, 87),
        ('javier', 41, 92),
        ('ana', 39, 76)
    ]
    cursor.executemany("INSERT INTO persona VALUES(NULL,?,?,?)", data)
    conn.commit()
    conn.close()
    
    
if __name__ == '__main__':
    createdb()
    agregar()
    