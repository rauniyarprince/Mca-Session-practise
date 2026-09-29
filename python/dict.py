# Program to demonstrate student dictionary operations

student = {
    "name": "Rahul",
    "age": 22,
    "course": "MCA",
    "marks": 85
}

print("Original Dictionary:")
print(student)

# Add an entry
student["city"] = "Delhi"

# Update an entry
student["marks"] = 90

# Delete an entry
del student["age"]

# Search for an entry
key = "name"

if key in student:
    print("\n", key, "=", student[key])
else:
    print("\nEntry not found")

# Traverse dictionary
print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)