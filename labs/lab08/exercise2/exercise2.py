# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    list1 = open(file1, 'r')
    list2 = open(file2, 'r')
    output = open(output_file, "w")

    names_list1 = set(list1.readlines())
    names_list2 = set(list2.readlines())
    completed_list = list(names_list1|names_list2)
    completed_list = sorted(completed_list)

    result = 0
    for name in completed_list:
        output.write(name)
        result += 1

    list1.close()
    list2.close()
    output.close()
    return result


# Test your code here
result = merge_lists("labs/lab08/exercise2/data/list1.txt", "labs/lab08/exercise2/data/list2.txt", "labs/lab08/exercise2/data/merged.txt")
print(f"Unique names: {result}")
