#--------------------------------------------------------------- IMPORT MODULES ----------------------------------------------------------------

import time
import os

#---------------------------------------------------------- SET VARIABLES + FUNCTIONS ----------------------------------------------------------

total = 0
finalTotal = 0
foodChoices = {}

def calculateTotal(): # Function for main shopping loop where user can choose multiple items which are added together to produce the total cost
    global total
    global foodChoices
    Checkout = False

    while Checkout == False:
        print("""
 _________________
| ---FOOD LIST--- |
| 1. Yoghurt $2   |
| 2. Meat Pie $5  |
| 3. Burger $6    |
 _________________""")
        choice = input("""
Select an item (1/2/3): """)
        if choice == '1':
            print(f"""
Yoghurt added to cart!""")
            total += 2
            foodChoices.update({'Yoghurt' : 2})
        elif choice == '2':
            print(f"""
Meat Pie added to cart!""")
            total += 5
            foodChoices.update({'Meat Pie' : 5})
        elif choice == '3':
            print(f"""
Burger added to cart!""")
            foodChoices.update({'Burger' : 6})
            total += 6
        else:
            print("""
Invalid input. Enter a number from 1-3 (1/2/3).""")
        time.sleep(1.5)
        response = input("Head to checkout? (yes/no): ")
        if response.lower() == 'yes':
            Checkout = True
        elif response.lower() != 'yes' and response.lower() != 'no':
            print("""
Invalid input. Enter yes/no.""")
        time.sleep(1.5)
        os.system('cls')

def applyDiscount(): # Function for checking if total after checkout is applicable for discount and returning a rounded final total cost
    global finalTotal
    global total 
    if total > 10:
        finalTotal = round(total * 0.9, 2)
        print("""
Discount for orders above $10 was applicable!""")
    else:
        finalTotal = round(total, 2)
    time.sleep(1.5)
    print(f"""
_______________________________________________________
   Your final total is ${finalTotal}. Printing receipt... 
_______________________________________________________""")




#----------------------------------------------------------------- MAIN LOOP ------------------------------------------------------------------

studentName = input("""Enter full student name: """) 
time.sleep(2)
print(f"""
 _____________________________________________________
  Welcome {studentName}! Loading canteen item list... 
 _____________________________________________________""")
time.sleep(2)
calculateTotal()
applyDiscount()
time.sleep(1.5)
print(f"""                   
 _____________________      
| ----- RECEIPT ----- |
|                     |
| {studentName}       
| ${finalTotal} 
|                     |""")
for key, value in foodChoices.items():
    print(f"| {key}, ${value}")
print("""|                     |
|                     |
|                     |
|                     |
 _____________________""")

