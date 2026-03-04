# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    f = open(products_file, 'r')
    g = open(order_file, 'r')
    output = open(output_file, "w")

    product_reader = csv.reader(f)
    
    order_reader = csv.reader(g)





    f.close()
    g.close()
    output.close()
    return

# Test your code here
result = calculate_order_total("data/products.csv", "data/order.csv", "data/total.csv")
print(f"Grand total: ${result:.2f}")
