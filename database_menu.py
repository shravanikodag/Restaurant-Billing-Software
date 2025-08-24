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
price INTEGER NOT NULL,
gst INTEGER NOT NULL,
category TEXT)''')


#3.sample menu
menu_items=[
    #Starters
    ('Veg Momos',129,5,'Starter'),
    ("Tomato Soup",99,5,"Starter"),
    ("Greek Salad",139,5,"Starter"),
    ("Garlic Bread",129,5,"Starter"),
    ("Panner Chiili Dry",199,5,"Starter"),
    ("Crispy Corn",99,5,"Starter"),
    ("Veg Manchurian",199,5,"Starter"),

    #Main Course
    ("Veg Kolhapuri",199,5,"Main Course"),
    ("Malai Kofta",244,5,"Main Course"),
    ("Palak Panner",299,5,"Main Course"),
    ("Dal Tadka",129,5,"Main Course"),
    ("Mix Veg",139,5,"Main Course"),
    ("Veg Hakka Noodles",179,5,"Main Course"),
    #Roti
    ("Naan",10,2,"Roti"),
    ("Butter Roti",15,3,"Roti"),
    ("Cheese Roti",12,2,"Roti"),
    #Rice
    ("Jeera Rice",149,5,"Rice"),
    ("Steam Rice",99,5,"Rice"),
    ("Veg Biryani",299,5,"Rice"),
    #Beavrage
    ("Cold Coffee",40,5,"Beavrage"),
    ("Fresh Lime Soda",49,5,"Beavrage"),
    ("Mango Lassi",69,5,"Beavrage"),
    ("Masala Chai",15,5,"Beavrage"),
    #Dessert
    ("Gulabjamun(2pcs)",99,5,"Dessert"),
    ("RassMalai(2pcs)",149,5,"Dessert"),
    ("Caramel Custard",99,5,"Dessert"),
    ("Ice Cream Scoop",79,5,"Dessert"),
    ("Chocolate Brownie",129,5,"Dessert")
]

#4.insert sample menu into  table
cursor.executemany('''INSERT INTO MENU (item_name,price,gst,category)
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
