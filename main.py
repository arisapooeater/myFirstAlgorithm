import time
total = 0
finalTotal = 0

def calculateTotal():
    global total
    Checkout = False
    foodChoices = []

    while Checkout == False:
        print("""
 _________________
| ---FOOD LIST--- |
| 1. Yoghurt $2   |
| 2. Meat Pie $5  |
| 3. Burger $6    |
 _________________""")
        choice = int(input("""
Select an item (1/2/3): """))
        if choice == 1:
            print(f"""
Yoghurt added to cart!""")
            total += 2
        elif choice == 2:
            print(f"""
Meat Pie added to cart!""")
            total += 5
        elif choice == 3:
            print(f"""
Burger added to cart!""")
            total += 6
        else:
            print("""
Invalid input. Enter a number from 1-3 (1/2/3).""")
        response = input("Head to checkout? (yes/no): ")
        if response.lower() == 'yes':
            Checkout = True
        elif response.lower() != 'yes' or response.lower() != 'no':
            print("""
Invalid input. Enter yes/no.""")
        time.sleep(1.5)
            


def applyDiscount():
    global finalTotal
    global total 
    if total > 10:
        finalTotal = total * 0.9
        print("""
Discount for orders above $10 was applicable!""")
    else:
        finalTotal = total
    print(f"""
_______________________________________________________
   Your final total is ${finalTotal}. Printing receipt... 
_______________________________________________________""")

    


studentName = input("""Enter full student name: """)
time.sleep(2)
print(f"""
 _____________________________________________________
  Welcome {studentName}! Loading canteen item list... 
 _____________________________________________________""")
time.sleep(2)
calculateTotal()
applyDiscount()
print(f"""
 _____________________      
| ----- RECEIPT ----- |
|                     |
| {studentName}       
| ${finalTotal}       
|                     |
|                     |
|                     |
|                     |
 _____________________""")

