products = []
def read_data() :
    f = open(' C:\Users\nooshi\Desktop\python\session8','r')
    for l in f :
        product = l.split(',')
        dic = {'ID': product[0],'Name': product[1],'Price':product[2] ,'Count':product[3]}
        products.append(dic)

print("welcome my friend!")

def show_menu () :
    while True:
        print('1- Add')
        print('2- Delete')
        print('3- Search')
        print('4- Buy')
        print('5- Edit')
        print('6-products')
        print('7- Exit')
       
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            add()
        elif user_choice == 2:
            delete()
        elif user_choice == 3:
            search()
        elif user_choice == 4:
            buy()
        elif user_choice == 5:
            edit()
        elif user_choice == 6:
            show_products()
        elif user_choice == 7:
            break
        else:
            print('please choose again...')

def add():
    while True:
        id = input('Enter the ID you wanna add (Enter f to finish):')
        if id == 'f': 
            break
        name =input('Enter Name:')
        for p in products:
            if p['ID'] == id and p['Name'] == name:
                print(f"Product with ID '{id}' and name '{name}' already exists!")
                return
            if p['ID'] == id and p['Name'] != name:
                print(f"Product with ID '{id}' already exists with different name!")
                return
            if p['ID'] != id and p['Name'] == name:
                print(f"Product with name '{name}' already exists with different ID!")
                return
        price =input('Enter Price:')
        count =input('Enter Count:')
        dic = {'ID':id, 'Name':name, 'Price':price, 'Count': count}
        products.append(dic)
        with open(' C:\Users\nooshi\Desktop\python\session8', 'a') as f:  
            line = f"{id},{name},{price},{count}\n"
            f.write(line)
        print('Product added successfully!')

def delete():
    while True:
        id = input('Enter the ID you wanna remove (Enter f to finish):')
        if id == 'f': 
            break
        with open(' C:\Users\nooshi\Desktop\python\session8', 'r') as f:
            lines = f.readlines()
        with open(' C:\Users\nooshi\Desktop\python\session8', 'w') as f:
            for line in lines:
                if line.split(',')[0] != id:
                    f.write(line)
        print('Product removed successfully!')

def search():
    while True:
        key = input('Enter your key (Enter f to finish):')
        if key == 'f': 
            break
        for product in products :
            if key == product['ID'] or key == product['Name'] or key == product['Price'] or key == product['Count']:
                print(product)
                break
        else:
            print('Not Found')

def buy():
    cart = []
    total_price = 0
    while True: 
        item_id = input("Enter the ID of item you want to buy (Enter 'f' to finish):")
        if item_id == 'f': 
            break
        item_found = False
        for product in products:
            if product["ID"] == item_id:
                item_found = True
                count = int(input("Enter the quantity:"))
                if int(product["Count"]) >= count:
                    product["Count"] = str(int(product["Count"]) - count)
                    cart.append({"Name":product["Name"],
                                 "Price":product["Price"],
                                 "Count":count})
                    print("Added to cart!")
                    total_price += int(product["Price"]) * count

                else:
                    print("Current stock:", product["Count"])
        if not item_found:
                print("Sorry, we don't have a product with this ID.")

    print("Cart:", cart)
    print("Total price:", total_price, "Tomans")

    with open(" C:\Users\nooshi\Desktop\python\session8", "w") as f:
        for product in products:
            f.write(product["ID"]+","+product["Name"]+","+product["Price"]+","+product["Count"]+"\n")
def edit():
    while True:
        id = input("Enter the ID of the product you wanna edit (Enter f to finish):")
        if id == 'f':
            return

        for product in products:
            if product['ID'] == id:
                print(" ")
                print('product:')
                print('ID\t Name \t Price \t Count')
                print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
                print(" ")
                while True:
                    print('1- Name')
                    print('2- Price')
                    print('3- Count')
                    choice = input('Which field do you want to edit?')

                    if choice == '1':
                        new_name = input('Enter new name:')
                        product['Name'] = new_name
                        break

                    elif choice == '2':
                        new_price = input('Enter new price:')
                        product['Price'] = new_price
                        break

                    elif choice == '3':
                        new_count = input('Enter new count:')
                        product['Count'] = new_count
                        break

                    else:
                        print('Invalid choice. Please enter 1/2/3.')

                with open(' C:\Users\nooshi\Desktop\python\session8', 'w') as f:
                    for product in products:
                        line = f"{product['ID']},{product['Name']},{product['Price']},{product['Count']}\n"
                        f.write(line)
                
                print('Product updated successfully!')
                break
            
        else:
            print('Product not found. Please enter a valid ID.')

def show_products() :
    print('ID \t Name \t Price \t Count')
    for product in products :
        print(product['ID'],'\t',product['Name'],'\t',product['Price'],'\t',product['Count'])
read_data()
show_menu()

