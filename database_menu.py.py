import sqlite3
# 1.connect to database (it will create database folder &file if not exists)
conn=sqlite3.connect('database/restaurant.db')
cursor=conn.cursor()
#2.Create menu table
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu(
id INTEGER PRIMARY KEY,
item_name TEXT NOT NULL,
category TEXT,
price REAL NOT NULL,
gst REAL)''')
#3.sample menu
menu_items=[
     ('Panner-tikka','Starter',150,5),
     ('veg manchurian','starter',150,6),
     ('veg soup','starter',150,2),
     ('Panner butter  masala ','main course',150,6),
     ('dal tadka','main course',100,5),
     ('veg biryani','main course',350,6),
     ('butter roti','bread',20,5),
     ('paratha','bread',45,6),
     ('butter naan','bread',30,4),
     
]
#4.insert sample menu into  table
cursor.executemany('''INSERT INTO MENU (item_name,category,price,gst)
VALUES(?,?,?,?)''',menu_items)
#5.save change
conn.commit()
#6.fetch and show all menu items
cursor.execute("SELECT * FROM menu")
rows=cursor.fetchall()
print("MENU ITEMS:")
for row in rows:
    print(row)
#7.close connection
'''cursor.execute("DELETE FROM menu")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='menu'")

conn.commit()
print("deleted")'''
conn.close()
