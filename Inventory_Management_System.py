"""
--------------------------------------------------------------------
 Project Title      : Inventory Management System
 Programming language: Python
 Author             Amanuel Kindalem
 For:Fulfillment of basic Understanding Online Python Course
 Date              : October 21, 2025 G.C
--------------------------------------------------------------------

 Description:
 ------------
 This program implements a bilingual (English and Afan Oromo) Inventory 
 Management System using Python. It uses file handling to store data 
 persistently. The system allows users to add, update, delete, view,
 and search products by their ID.

 The program is designed using classes/functions, lists, input validation,
 and file handling operations.
--------------------------------------------------------------------
"""

# Class to represent Product (similar to struct in C++)
class Product:
    def __init__(self, id=0, name="", category="", price=0.0, quantity=0):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


# Global Variables
inventory = [Product() for _ in range(10000)]  # List of Product objects
productCount = 0
language = 1


# Input Validation Functions
def getintinput(prompt):
    global language
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                break
            else:
                print("Invalid input. Enter a positive integer." if language == 1
                      else "Galchi sirrii miti. Lakkoofsa sirrii galchi.")
        except ValueError:
            print("Invalid input. Enter a positive integer." if language == 1
                  else "Galchi sirrii miti. Lakkoofsa sirrii galchi.")
    return value


def getDoubleInput(prompt):
    global language
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                break
            else:
                print("Invalid input. Enter a positive number." if language == 1
                      else "Galchi sirrii miti. Lakkoofsa sirrii galchi.")
        except ValueError:
            print("Invalid input. Enter a positive number." if language == 1
                  else "Galchi sirrii miti. Lakkoofsa sirrii galchi.")
    return value


def getStringInput(prompt):
    global language
    value = input(prompt)
    while value == "":
        print("Input cannot be empty. Try again: " if language == 1
              else "Galchi duwwaa miti. Irra deebi'i galchi: ", end="")
        value = input()
    return value


# loadFromFile function used for input/load data from file
def loadFromFile():
    global productCount, inventory
    try:
        with open("inventory.txt", "r") as in_file:
            productCount = int(in_file.readline().strip())

            for i in range(productCount):
                inventory[i].id = int(in_file.readline().strip())
                inventory[i].name = in_file.readline().strip()
                inventory[i].category = in_file.readline().strip()
                inventory[i].price = float(in_file.readline().strip())
                inventory[i].quantity = int(in_file.readline().strip())
    except FileNotFoundError:
        return  # File not found
    except:
        pass


# saveToFile function used for store data in the file persistently
def saveToFile():
    global productCount, inventory
    with open("inventory.txt", "w") as out_file:
        out_file.write(str(productCount) + "\n")
        for i in range(productCount):
            out_file.write(str(inventory[i].id) + "\n")
            out_file.write(inventory[i].name + "\n")
            out_file.write(inventory[i].category + "\n")
            out_file.write(str(inventory[i].price) + "\n")
            out_file.write(str(inventory[i].quantity) + "\n")


# findProductById function used for search a desired product by ID
def findProductById(id):
    global productCount, inventory
    for i in range(productCount):
        if inventory[i].id == id:
            return i  # Index of product
    return -1  # Not found


# Add Product function used for adding a discovered new product
def addProduct():
    global productCount, inventory, language

    id = getintinput("Enter product ID: " if language == 1 else "ID oomishaa galchi: ")
    if findProductById(id) != -1:
        print("Product already exists.\n" if language == 1
              else "Oomishni duraan jira.\n")
        return

    p = Product()
    p.id = id
    p.name = getStringInput("Enter product name: " if language == 1
                            else "Maqaa oomishaa galchi: ")
    p.category = getStringInput("Enter category: " if language == 1
                                else "Ramaddii galchi: ")
    p.price = getDoubleInput("Enter price (ETB): " if language == 1
                             else "Gatii (ETB) galchi: ")
    p.quantity = getintinput("Enter quantity: " if language == 1
                             else "Baay'ina galchi: ")

    inventory[productCount] = p
    productCount += 1
    saveToFile()
    print("Product added successfully.\n" if language == 1
          else "Oomishni milkaa'inaan dabalameera.\n")


# Remove Product function used for delete the products currently not found in the system
def removeProduct():
    global productCount, inventory, language

    id = getintinput("Enter product ID to remove: " if language == 1
                     else "ID oomishaa haquuf galchi: ")
    index = findProductById(id)
    if index == -1:
        print("Product not found.\n" if language == 1
              else "Oomisha hin argamne.\n")
        return

    for i in range(index, productCount - 1):
        inventory[i] = inventory[i + 1]
    productCount -= 1
    saveToFile()
    print("Product removed successfully.\n" if language == 1
          else "Oomishni milkaa'inaan haqameera.\n")


# Update Product functions used for updating a products information found in the system
def updateProduct():
    global inventory, language

    id = getintinput("Enter product ID to update: " if language == 1
                     else "ID oomishaa haaromsuuf galchi: ")
    i = findProductById(id)
    if i == -1:
        print("Product not found.\n" if language == 1
              else "Oomisha hin argamne.\n")
        return

    inventory[i].name = getStringInput("New name: " if language == 1
                                       else "Maqaa haaraa: ")
    inventory[i].category = getStringInput("New category: " if language == 1
                                           else "Ramaddii haaraa: ")
    inventory[i].price = getDoubleInput("New price: " if language == 1
                                        else "Gatii haaraa: ")
    inventory[i].quantity = getintinput("New quantity: " if language == 1
                                        else "Baay'ina haaraa: ")

    saveToFile()
    print("Product updated.\n" if language == 1
          else "Oomishni haaromfameera.\n")


# View Products functions used for to see all the products found in our system
def viewProducts():
    global productCount, inventory, language

    if productCount == 0:
        print("Inventory is empty.\n" if language == 1
              else "Inventariin duwwaa dha.\n")
        return

    for i in range(productCount):
        print("\nID:", inventory[i].id)
        print(("Name: " if language == 1 else "Maqaa: "), inventory[i].name)
        print(("Category: " if language == 1 else "Ramaddii: "), inventory[i].category)
        print(("Price: ETB " if language == 1 else "Gatii: ETB "), inventory[i].price)
        print(("Quantity: " if language == 1 else "Baay'ina: "), inventory[i].quantity)


# Search Product functions used for finding a desired product from our system
def searchProduct():
    global inventory, language

    id = getintinput("Enter product ID to search: " if language == 1
                     else "ID oomishaa barbaadu galchi: ")
    i = findProductById(id)
    if i == -1:
        print("Product not found.\n" if language == 1
              else "Oomisha hin argamne.\n")
    else:
        print(("Product found: " if language == 1 else "Oomisha argame: "),
              inventory[i].name)


# Show Menu function used for shows the options implement in this program
def showMenu():
    global language

    while True:
        if language == 1:
            print("\nInventory Menu (English)")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. Update Product")
            print("4. View Products")
            print("5. Search Product")
            print("Q. Quit")
            print("Choice: ", end="")
        else:
            print("\nSirna Inventarii (Afaan Oromoo)")
            print("1. Oomisha dabali")
            print("2. Oomisha haqi")
            print("3. Oomisha haaromsi")
            print("4. Oomisha ilaali")
            print("5. Oomisha barbaadi")
            print("Q. Bahii")
            print("Filannoo kee: ", end="")

        ch = input().strip()

        if (ch >= '1' and ch <= '5') or ch.upper() == 'Q':
            if ch == '1':
                addProduct()
            elif ch == '2':
                removeProduct()
            elif ch == '3':
                updateProduct()
            elif ch == '4':
                viewProducts()
            elif ch == '5':
                searchProduct()
            elif ch.upper() == 'Q':
                break
        else:
            print("Invalid choice. Please try again.\n" if language == 1
                  else "Filannoo sirrii miti. Irra deebi'ii yaali.\n")


# main function
def main():
    global language

    loadFromFile()

    print("Choose Language / Afaan Filadhu")
    print("1. English")
    print("2. Afaan Oromo")

    while True:
        language = getintinput("Choice / Filannoo: ")
        if language == 1 or language == 2:
            break
        print("Invalid choice. Try again.\n" if language == 1
              else "Filannoo sirrii miti. Irra deebi'ii yaali.\n")

    showMenu()


if __name__ == "__main__":
    main()