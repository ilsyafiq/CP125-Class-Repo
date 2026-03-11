# Lab 08 Exercise 4: Student Grade Calculator
# Write your code below:
import csv
def calculate_final_grades(input_file, output_file):
    f = open(input_file, 'r')
    g = open(output_file, 'w')
    g.write("student_id,final_grade\n")

    product_reader = csv.reader(f)
    next(product_reader)
    total = 0
    count = 0
    for row in product_reader:
        final_grade = (float(row[1])*0.4) + (float(row[2])*0.6)
        g.write(f"{row[0]},{final_grade:.2f}\n")
        total += final_grade
        count += 1
    
    f.close()
    g.close()
    return total/count


# Test your code here
result = calculate_final_grades("labs/lab08/exercise4/data/scores.csv", "labs/lab08/exercise4/data/grades.csv")
print(f"Average final grade: {result:.2f}")
