# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    f = open(input_file, 'r')
    h = open(output_file, "w")

    individual_scores = f.readlines()
    student_dict = {}
    for student_result in individual_scores:
        splitted = student_result.split()
        student_dict[splitted[0]] = splitted[1]
    
    result = 0
    for student in student_dict:
        if int(student_dict[student]) >= 80:
            h.write(f"{student} {student_dict[student]}\n")
            result += 1
            
    f.close()
    h.close()
    return result

# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
