import sqlite3
# 1.connect to database (it will create database folder &file if not exists)
conn=sqlite3.connect('database/restaurant.db')
cursor=conn.cursor()


#CLEAR EXISTING MENU
cursor.execute("DELETE FROM menu")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='menu'")


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
     ('Veg Manchurian','Starter',150,6),
     ('Veg Soup','Starter',150,2),
     ('Panner Butter Masala ','Main Course',150,6),
     ('Dal Tadka','Main Course',100,5),
     ('Veg Biryani','Main Course',350,6),
     ('Butter Roti','Bread',20,5),
     ('Paratha','Bread',45,6),
     ('Butter Naan','Bread',30,4),
     ('Jeera Rice','Rice',120,5),
     ('Steam Rice','Rice',100,4),
     ('Gulab Jamun','Desert',50,3),
     ('Ice Cream','Desert',100,5),
     ('Rasgulla','Desert',120,5)   
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
conn.close()
