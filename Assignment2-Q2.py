products = {
"Electronics": {"Laptop": 1200, "Phone": 800},
"Clothes": {"Shirt": 50, "Shoes": 100},
"Grocery": {"Rice": 20, "Milk": 10}
}
maxprice=0
maxproduct=""

for category in products:
    for product in products[category]:
        if products[category][product] > maxprice:
            maxprice = products[category][product]
            maxproduct = product

print(maxproduct,"",maxprice)
