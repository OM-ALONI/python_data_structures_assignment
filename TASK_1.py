# Task 1: Create a Dictionary of Student Marks

# Step 1: Create the dictionary
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Step 2: Ask user for student name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or display message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")
