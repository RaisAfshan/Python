class ShoppingCart():

    def add_item(self,n):
        items = []

        for i in n:
            it = input("enter the item")
            p = int(input("enter the price"))
            item = {}
            item["itemName"] = it
            item["itemPrice"] = p
            print(item)
            items.append(item)
        print(items)

obj = ShoppingCart()
n = input("enter the number of items")
obj.add_item(n)






