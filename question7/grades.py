
import csv


def append_new_students(new_file, target_file):
    new_student = open(new_file, 'r')
    final = open(target_file, 'a')
    new_reader = csv.reader(new_student)
    target_writer = csv.writer(final)
    for row in new_reader:
        target_writer.writerow(row)