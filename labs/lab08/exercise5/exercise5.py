# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv
def summarize_sales(input_file, output_file):
    f = open(input_file, 'r')
    g = open(output_file, 'w')

    product_reader = csv.reader(f)
    next(product_reader)
    total_revenue = 0
    count = 0
    max = 0
    min = 9999999
    for row in product_reader:
        revenue = float(row[1]) * float(row[2])
        total_revenue += revenue
        count += 1
        if revenue > max:
            max = revenue
        if revenue < min:
            min = revenue
    average = total_revenue/count
    g.write(f"Total Revenue: ${total_revenue:.2f}\n")
    g.write(f"Average Revenue: ${average:.2f}\n")
    g.write(f"Highest Revenue: ${max:.2f}\n")
    g.write(f"Lowest Revenue: ${min:.2f}")

    return (total_revenue, average, max, min)
# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
