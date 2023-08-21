print(f"A product with name {'name'} already exists.")
  

new_product = {"id": int(id), "name": name,"price": price, "count": count}
products.append(new_product)
print("The product has been added successfully.")


def delete():
     id = input("Enter the id of the product you want to delete: ")
     for product in products:
        if id == str(product["id"]):
            products.remove(product)
            print("The product has been deleted successfully.")
                 

     print(f"A product with ID {id} does not exist.")


def edit():
    id = input("Enter the id of the product you want to edit: ")
    for product in products:
        if id == str(product["id"]):
            product["name"] = input("Enter the new name: ")
            product["price"] = int(input("Enter the new price: "))
            product["count"] = int(input("Enter the new count: "))
            print("The product has been edited successfully.")
            return

    print(f"A product with ID {id} does not exist.")


def search():
    term = input("Enter a search term: ")
    results = []
    for product in products:
        if term.lower() in product["name"].lower():
            results.append(product)

    if len(results) == 0:
        print("No matching products found.")
    else:
        print(" id \t   name \t price \t\tcount")
        for product in results:
            print(product["id"], "\t", product["name"], "\t",
                  product["price"], "\t\t", product["count"])


def buy():
    id = input("Enter the id of the product you want to buy: ")
    for product in products:
        if id == str(product["id"]):
            count = int(input("Enter the count you want to buy: "))
            if count > product["count"]:
                print("There is not enough stock.")
                return
            else:
                product["count"] -= count
                print(
                    f"You have purchased {count} {product['name']}(s) for {count * product['price']}.")
                return

    print(f"A product with ID {id} does not exist.")

read_data()
show_menu()
