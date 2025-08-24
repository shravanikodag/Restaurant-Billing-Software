import sqlite3
from fpdf import FPDF
from datetime import datetime
import os

#---------SHOW MENU--------
def show_menu():
    #connecting to database  
    conn=sqlite3.connect('database/restaurant.db')
    cur = conn.cursor()
    cur.execute("SELECT id, item_name, price, gst,category FROM menu ORDER BY category,id")
    items = cur.fetchall()
     
    print("\n"+"="*70)
    print("🍽WELCOME TO THE TEST TERRACE RESTAURANT MENU🍽".center(80))
    print("="*70)
    current_category = None

    for  item in items:
        id, item_name, price,gst, category=item
        if category != current_category:
            current_category = category
            print(f"{current_category.upper()}")
            print("-"*70)
            print(f"{'ID':<5}{'ITEM NAME':25}{'PRICE':<10}{'GST':<6}")
        # price without .0
        print(f"{id:>5}. {item_name:<25}₹{int(price)}/-{'':<3}{int(gst)}%")
    print("="*70)
    conn.close()
    return items


def generate_bill(order_list):
    conn=sqlite3.connect("database/restaurant.db")
    cursor=conn.cursor()
    bill_items=[]
    total=0
    for item_id,qty in order_list:
        cursor.execute("SELECT item_name,price,gst FROM  menu WHERE id=?",(item_id,))
        result=cursor.fetchone()
        print(result)
        if result:
            name,price,gst=result
            gst_amount =(price*gst)/100  #calculate GST amount
            final_price=(price + gst_amount)*qty
            total=total+final_price
             #save details for bill
            bill_items.append((name,qty,price,gst,final_price))
        else:
            print(f"Item with ID {item_id} not found in menu!")
    conn.close()
    return bill_items,total


def create_pdf(bill_items,total,customer_info):
    #create pdf object
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Times","B",14)

    #Title of bill
    pdf.cell(0,10,txt="THE TEST TERRACE",ln=True,align="C")

    #Data and time
    pdf.set_font("Times","I",14)
    pdf.cell(0,10,f"Data: {datetime.now().strftime('%Y-%m-%d')}",ln=True,align="R")
    pdf.ln(2) #add blank line
    
    #customer info
    pdf.set_font("Times","",12)
    pdf.cell(0,10,f"Customer Name:{customer_info['name']}",ln=True,align="L")
    pdf.cell(0,10,f"Customer Contact:{customer_info['contact']}",ln=True,align="L")
    pdf.cell(0,10,f"Order Type:{customer_info['order_type']}",ln=True,align="L")
    pdf.ln()
    
    #Table headers
    pdf.set_font("Times","B",12)
    pdf.cell(60,10,"Items",border=1) #item name
    pdf.cell(20,10,"Quantity",border=1,align="C") #Quantity
    pdf.cell(30,10,"Price",border=1,align="C") #item quantity
    pdf.cell(20,10,"GST%",border=1,align="C") #GST%
    pdf.cell(40,10,"Total",border=1,align="C") #Total
    pdf.ln()
    #TBLE ROW
    pdf.set_font("Times","",12)
    for item in bill_items:
        pdf.cell(60,10,item[0],border=1) #item name
        pdf.cell(20,10,str(item[1]),border=1,align="C") #Quantity
        pdf.cell(30,10,f"Rs{item[2]}",border=1,align="C") #item price
        pdf.cell(20,10,f"{item[3]}%",border=1,align="C") #GST%
        pdf.cell(40,10,f"Rs{round(item[4],2)}",border=1,align="C") #Total
        pdf.ln()
    #final total
    pdf.set_font("Times","B",14)
    pdf.cell(0,10,txt=f"Total Amount: Rs{round(total,2)}", ln=True, align="R")

    #Save pdf
    if not os.path.exists("receipts"):
        os.makedirs("receipts")
    timestamp=datetime.now().strftime("%Y%m%d_%H%M%S")
    filename=f"receipts/bill{timestamp}.pdf"
    pdf.output(filename)
    
    print("\n Bill generated successfully! Check file:bill.pdf")

def validate_item_id(item_id,items):
    valid_ids=[item[0] for item in items]
    return item_id in valid_ids

#---------MAIN PROGRAM------------

if __name__=="__main__":
    try:
        if not os.path.exists("database/restaurant.db"):
            print("Error: database file not found!")
            print("Please make sure 'database/restaurant.db' exists in your folder.")
            exit()
        menu_str=show_menu()
        if not menu_str:
            print("no menu items found in database!")
            exit()
        order_list=[] 
        print("Enter your order ( item id and Quantity):")

    #Take orders from customers
        while True:
            try:
                choice=int(input("Enter Item id to order starts from 1:").strip())
                if choice==0:
                    break
                if not validate_item_id(choice,menu_str):
                    print(f"Invalid Item ID{choice}.Please choose from the menu.")
                    continue
                quantity=int(input("Enter Quantity: ").strip())
                if quantity<=0:
                    print("Quantity must be greater than 0")
                    continue
                order_list.append((choice,quantity))
                print(f"added to order: item.{choice},quantity:{quantity}")
            except ValueError:
                print("Invalid Input,try again")
            except Exception as e:
                print(f"An error occurred: {e}")

        #procceeing your bill
        if order_list:
            customer_info={}
            customer_info['name']=input("Enter Customer Name: ").strip()
            customer_info['contact']=input("Enter contact number:").strip()
            customer_info['order_type']=input("Order Type (Dine-in/Takeway):").strip()
            try:
                discount=float(input("Enter discount amonut (if any,else 0):").strip())
            except:
                discount=0.0
                customer_info['discount']=discount
            print("\nGenerating your bill...")
            bill_items,total = generate_bill(order_list) #create bill
            if bill_items:
                print("\n=======================BILL SUMMARY=============================") 
                print(f"{'Item':20} {'quantity':<10} {'Price':<10} {'GST%':<10} {'Total':<10}")
                print("-"*60)
                grand_total=0
                for item in bill_items:
                    item_name,quantity,price,gst,item_total=item
                    print(f"{item_name:<20}{quantity:<10} Rs{price:<10} {gst:<10} {item_total:<9.2f}")
                    grand_total+=item_total
                print("-"*60)
                print(f"{'GRAND TOTAL:':<50}Rs{grand_total:.2f}")

                create_pdf(bill_items,total,customer_info) #create pdf
            else:
                print("No valid items found in your order")
        else:
            print("No items selected,bill not generated")
    except Exception as e:
        print(f"error:{e}")
        print("please check your database connection")
   


