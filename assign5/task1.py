# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Eve": 91
}

# Step 2: Ask the user to enter a student's name
student_name = input("Enter the student's name: ")

# Step 3: Check if the student's name is in the dictionary
if student_name in student_marks:
    # If the name is found, show their marks
    print(student_name + "'s marks: " + str(student_marks[student_name]))
else:
    # If the name is not found, show an error message
    print("Student " + student_name + " not found in the dictionary.")
