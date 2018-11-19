#Shopping List
shopping_list = []
print("What do you want to store in your list")

# Enter name of list items
items = raw_input("Enter items : ")

# Enter DONE to quit
while(items != "DONE"):
    # To add items
    shopping_list.append(items)
    
    # Take Input
    items = raw_input("Enter items : ")
    
# Printing shopping list
print("Here is your list")
for x in shopping_list:
    print(x)
