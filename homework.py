products= []


def read_data():
    f= open("/Users/shnik/Desktop/python/session7/text.txt", 'r')
    for i in f:
        product= i.split(",")
        dic = {'id':product[0],'name':product[1], 
             'price':product[2],'count':product[3]}
        #product.append(i)
        #print(result)
        products.append(dic)

def show_menu():
    print('1- add')
    print("2- delete")
    print('3- search')
    print('4- buy')
    print("5- edit")
    print('6- exit')
    print("7- show products")
def add():
    id=input("enter id: ")
    name=input("enter name: ")
    price=input("enter price: ")
    count=input("enter count")

    dic= {"id":id,  "name":name   ,"price":price  ,"count":count}
    products.append(dic)
    print(products)
def delete():
    while True:
        id = input('id kala ra vared konid:')
        
        with open('/Users/shnik/Desktop/python/session7/text.txt', 'r') as f:
            lines = f.readlines()
        with open('/Users/shnik/Desktop/python/session7/text.txt', 'r') as f:
            for line in lines:
                if line.split(' , ')[0] != id:
                    f.write(line)
        print('kala ba movafaghiat hazf shod!')

def search():
    key=input("enter your key: ")
    for product in products:
        if key == product['id'] or key ==product['name']:
          print(product)
          break
    else:
        print("not found")


def buy():
    cart = []
    while True:
        id = input(
            "id kala morede nazare khod ra vared konid (ya 'khoruj'  ta code stop shavad) : ")
        if id == "khoruj":
            break

        found = False
        for product in products:
            if int(id) == product["id"]:
                found = True
                count_to_buy = int(input(
                    "tedade morede niaz khod ra vared konid: "))

                if count_to_buy > product["count"]:
                    print(
                        f"mojudi kafi nmibashad {product['name']} (ID: {product['id']})")
                    break
                else:
                    product["count"] = product["count"] - count_to_buy
                    item = {
                        "id": product["id"],
                        "name": product["name"],
                        "price": product["price"],
                        "count": count_to_buy
                    }
                    cart.append(item)
                    break

        if not found:
            print(f"id:{id} mojud nmibashad .")

        print("kharide shoma: ")
        for item in cart:
            print(
                f"\t gheimate har {item['name']}: {item['price']} Toman / {item['count']} of {item['name']} (ID: {item['id']}) \t majmue kharide shoma: {item['count'] * item['price']} Toman mibashad.")

    total_cost = 0
    for item in cart:
        total_cost = total_cost + (int(item["count"]) * int(item["price"]))
    print(f"majmue factore shoma {total_cost} Toman mibashad.")



def edit():
    Id= input('id kala morede nazar ra vared konid: ')
    for product in products:
        print(f"gheimat va id kala ra vared konid:  {id}:")
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Count: {product['count']}")            
        print("1- Name")
        print("2- gheimat")
        print("3- tedad")
        item_to_edit = int(
                input("shomare morede nazar ra vared konid: "))

        if item_to_edit == 1:
                new_name = input("new name: ")
                product["name"] = new_name
                print(
                    f"name kala ba id {id} taghir krd be {new_name}.")
        elif item_to_edit == 2:
                new_price = int(input("gheimate jadid ra vared konid: "))
                product["price"] = new_price
                print(
                    f"gheimate jadide kal  {id} taghir krd be {new_price}.")
        elif item_to_edit == 3:
                new_count = int(input("tedad jadid: "))
                product["count"] = new_count
                print(
                    f"tedad kala ba {id} taghir krd be {new_count}.")
        break
    else:
        print(f" code kala eshtebah ast.")
        return

    print("taghirat ba movafaghiat anjam shod:D")

def exit():
    pass
def showproducts():
    print('id\t name\t  price\t  count')
    for product in products:
        print(product['id'],'\t',product['name'], 
              '\t' , product['price'], '\t', product["count"])
        print(f"{product['id']}\t {product['name']}")

read_data()
show_menu()

user_choice= int(input("enetr your chooise: "))
if user_choice==1:
    add()
elif user_choice==2:
    delete()
elif user_choice==3:
    search()
elif user_choice==4:
    buy()
elif user_choice==5:
    edit()
elif user_choice==6:
    exit()
elif user_choice==7:
    showproducts()    

else:
    print("wrong number! ")                

