products = [
 ("Laptop", 1200),
 ("Mouse", 25),
 ("Keyboard", 45),
 ("Monitor", 300),
 ("USB Cable", 10)
 ]
 
def more_than_100(products):
    product,price = products
    return price > 100

products_price_more_than_100 = list(filter(more_than_100,products))
print(products_price_more_than_100)

sum_of_amount = 0
for product,price in products:
    sum_of_amount = sum_of_amount + price
    
print(f"The total amount is : {sum_of_amount}")

for product,price in products:
    print(f"Product: {product} - Price: {price}")
