# Lab 08 Exercise 1: Simple Score Filter
# Write your code below:

def filter_passing_scores(input_file, output_file):
    f = open(input_file, 'r')
    g = open(output_file, "w")
    scores = list(f.readlines())
    student_scores = {}
    for i in range(0, len(scores), 2):
        student_scores[scores[i].strip()] = scores[i + 1].strip()
    
    count = 0
    for student in student_scores:
        if float(student_scores[student]) >= 80:
            g.write(f"{student} {student_scores[student]}\n")
            count += 1

    print(student_scores)

    f.close()
    g.close()
    return count

# Test your code here
result = filter_passing_scores("labs/lab08/exercise1/data/scores.txt", "labs/lab08/exercise1/data/passing.txt")
print(f"Passing students: {result}")
