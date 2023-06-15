import os

ShoppingList = []

def mainScreen():
    print("Choose: ")
    print(" \
        ('m')enu to show the menu \n \
        ('v')iew the list \n \
        ('d')elete to remove product from list \n \
        ('q')uit the program \n ")
    
def viewList():
    print("Your list: ")
    for product in ShoppingList:
        print(product)

def addProduct(product):
    ShoppingList.append(product)


def deleteProduct(delProduct):
    ShoppingList.remove(delProduct)



mainScreen()
while True:
    product = input("Add the product or choose from menu: ")

    if product == "m":
            mainScreen()
            continue
    elif product == "v":
            viewList()
            continue
    elif product == "d":
            viewList()
            delProduct = input("Which product do you want to remove from the list? ")
            deleteProduct(delProduct)
            viewList()
            continue
    elif product == "q":
            viewList()
            print("Closed the list")
            break
    addProduct(product)

# create a new file - name = ShoppingList.txt 

f = open("ShoppingList.txt", "w")
for product in ShoppingList:
     f.write((product) + "\n" )   
f.close()
