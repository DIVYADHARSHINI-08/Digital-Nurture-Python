def cart(list1,list2):
    for i in range(len(list1)):
            print(f"{list1[i]} : {list2[i]}")
items = ["Onion", "Shampoo" , "Pouch"]
prices = [20, 150, 50]
print("Shopping Cart:")
cart(items,prices)