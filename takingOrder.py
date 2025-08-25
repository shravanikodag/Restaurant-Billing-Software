inPython 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\\Desktop\RestaurantBilling\Bill_generator.py

======================================================================
                 🍽WELCOME TO THE TEST TERRACE RESTAURANT MENU🍽                  
======================================================================
BEAVRAGE
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
   20. Cold Coffee              ₹40/-   5%
   21. Fresh Lime Soda          ₹49/-   5%
   22. Mango Lassi              ₹69/-   5%
   23. Masala Chai              ₹15/-   5%
DESSERT
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
   24. Gulabjamun(2pcs)         ₹99/-   5%
   25. RassMalai(2pcs)          ₹149/-   5%
   26. Caramel Custard          ₹99/-   5%
   27. Ice Cream Scoop          ₹79/-   5%
   28. Chocolate Brownie        ₹129/-   5%
MAIN COURSE
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
    8. Veg Kolhapuri            ₹199/-   5%
    9. Malai Kofta              ₹244/-   5%
   10. Palak Panner             ₹299/-   5%
   11. Dal Tadka                ₹129/-   5%
   12. Mix Veg                  ₹139/-   5%
   13. Veg Hakka Noodles        ₹179/-   5%
RICE
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
   17. Jeera Rice               ₹149/-   5%
   18. Steam Rice               ₹99/-   5%
   19. Veg Biryani              ₹299/-   5%
ROTI
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
   14. Naan                     ₹10/-   2%
   15. Butter Roti              ₹15/-   3%
   16. Cheese Roti              ₹12/-   2%
STARTER
----------------------------------------------------------------------
ID   ITEM NAME                PRICE     GST   
    1. Veg Momos                ₹129/-   5%
    2. Tomato Soup              ₹99/-   5%
    3. Greek Salad              ₹139/-   5%
    4. Garlic Bread             ₹129/-   5%
    5. Panner Chiili Dry        ₹199/-   5%
    6. Crispy Corn              ₹99/-   5%
    7. Veg Manchurian           ₹199/-   5%
======================================================================
Enter your order ( item id and Quantity):
Enter Item id to order starts from 1:1
Enter Quantity: 5
added to order: item.1,quantity:5
Enter Item id to order starts from 1:12
Enter Quantity: 5
added to order: item.12,quantity:5
Enter Item id to order starts from 1:16
Enter Quantity: 10
added to order: item.16,quantity:10
Enter Item id to order starts from 1:19
Enter Quantity: 2
added to order: item.19,quantity:2
Enter Item id to order starts from 1:20
Enter Quantity: 4
added to order: item.20,quantity:4
Enter Item id to order starts from 1:27
Enter Quantity: 5
added to order: item.27,quantity:5
Enter Item id to order starts from 1:0
Enter Customer Name: Priya Rane
Enter contact number:9154632487
Order Type (Dine-in/Takeway):Dine in
payment Mode:UPI
Enter discount amonut (if any,else 0):30

Generating your bill...
('Veg Momos', 129.0, 5.0)
('Mix Veg', 139.0, 5.0)
('Cheese Roti', 12.0, 2.0)
('Veg Biryani', 299.0, 5.0)
('Cold Coffee', 40.0, 5.0)
('Ice Cream Scoop', 79.0, 5.0)

=======================BILL SUMMARY=============================
Item                 quantity   Price      GST%       Total     
------------------------------------------------------------
Veg Momos           5          Rs129.0      5.0        677.25   
Mix Veg             5          Rs139.0      5.0        729.75   
Cheese Roti         10         Rs12.0       2.0        122.40   
Veg Biryani         2          Rs299.0      5.0        627.90   
Cold Coffee         4          Rs40.0       5.0        168.00   
Ice Cream Scoop     5          Rs79.0       5.0        414.75   
------------------------------------------------------------
GRAND TOTAL:                                      Rs2740.05

 Bill generated successfully! Check file:bill.pdf
