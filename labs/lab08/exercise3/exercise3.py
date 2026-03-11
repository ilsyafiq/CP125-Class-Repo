# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    f = open(products_file, 'r')
    g = open(order_file, 'r')
    output = open(output_file, "w")
    output.write("product_id,total_cost\n")

    product_dict = {}

    product_reader = csv.reader(f)
    next(product_reader)
    for row in product_reader:
        product_dict[row[0]] = row[2]
    
    order_reader = csv.reader(g)
    next(order_reader)
    grand_total = 0
    for row in order_reader:
        total = float(row[1]) * float(product_dict[row[0]])
        output.write(f"{row[0]},{total:.2f}\n")
        grand_total += total



    f.close()
    g.close()
    output.close()
    return grand_total

# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
