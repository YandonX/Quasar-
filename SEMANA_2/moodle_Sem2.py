def add_product():
    inventory[name]={'Price': price, 'Quantity': quantity}

def show_inventory(inventory):
    if inventory:
        for name, details in inventory.items():
            print(f"Product: {name} Price: ${details['Price']} Quantity: {details['Quantity']}")
    else:
        print("The inventory is void")
    
        
def Calculate_total_price(inventory):
    types=0
    value=0
    products_quantity=0
    if len(inventory) ==0:
        print("You have not add anything")
        
    for name in inventory:
            value+= inventory[name]['Price']*inventory[name]['Quantity']
            products_quantity+= inventory[name]['Quantity']
            types+= 1
            print(f"You buy  {inventory[name]['Quantity']}  each one for:   ${inventory[name]['Price']}")
            print(f"you have add {types} types of products in total, and in total:  {products_quantity} products")
            print(f"The total value until now is:   ${value}")
        
value=0
option=0
inventory={}
print("This is your inventory: \n1- add product  \n2- print product  \n3- Calculate stadistics  \n4- out\n")
while option!=4:
    try: 
        option= int(input("1- Add  2- Show  3- Calculate  4- out\n"))
    except ValueError:
        print("Error, this option isn't correct")
        continue

    if option == 1:
        name= input("insert the name: ")
        try:
            price= int(input("insert the price: "))
            quantity= int(input("insert the quantity: "))
        except ValueError:
            print("the price should be a number")
            continue

        add_product()

    elif option == 2:
        show_inventory(inventory)

    elif option == 3:
        Calculate_total_price(inventory)

print(f"Thank you for buy here, this is your inventory: \n {inventory}")     
print(f"====== The total value is {value} ==========")
    #Esto es todo por hoy