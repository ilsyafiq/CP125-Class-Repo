import csv 
def append_top_performers(input_file, output_file):
    f = open(input_file, 'r')
    input_reader = csv.reader(f)
    output = open(output_file, "a")
    output_writer = csv.writer(output)
    print(input_reader)