def find_qualified_students(student_records, required_courses):
    qualified = []
    
    for student_id, completed in student_records:
        common = completed | required_courses
        
        if common == completed:
            qualified.append(student_id)
    

    
    return sorted(qualified)

student_records = students = [
        ("Z9", {"A", "B", "C"}),
        ("A1", {"A", "B", "C"}),
        ("M5", {"A", "B", "C"})
    ]
required_courses = {"A", "B"}
print(find_qualified_students(student_records, required_courses))