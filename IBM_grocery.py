Greetings = '''Dear <|NAME|>,
Welcome in Grocery Stoppers. 
I am happy to have you here!
Have a great day ahead!
'''
name = input("Enter Your Name\n")
Greetings = Greetings.replace("<|NAME|>", name)
print(Greetings)

Items = {
    "Ashirwad": {"Flour" : "180/-"},
    "Sugarfree": {"Sugar": "90/-"},
    "Fortune": {"Oil": "210/-"}
}
print("Options are ", Items)

grocery_history = []
stop = False

while not stop:
    name = input("item_name:\n")
    quantity = input("Quantity purchased:\n")
    cost = input("price per item:\n")

    grocery_item = {"item_name": name, "quantity": int(quantity), "cost": float(cost) }
    grocery_history.append(grocery_item)

    response = input("would you like to enter another item?\nType 'Y' for continue or 'N' to quit:\n")

    if response == 'N' :
        stop = True

grand_total = 0

for item in grocery_history:
    item_total = item['quantity'] * item['cost']
    grand_total += item_total #if we want to keep coding lesser or simple you can add values directly without assigning the variable by giving += operator together
    print("%d %s @ ₹%f ₹%f" %(item['quantity'], item['item_name'], item['cost'], item_total)) #to match the output information like 1 oil @ $1.42 we use this signs in the code

    item_total = 0

print("Grand Total: ₹%f" % grand_total)






