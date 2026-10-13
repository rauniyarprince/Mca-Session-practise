# Create a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

# 1. Display dictionary
print("Dictionary:", student)

# 2. Access a value
print("Name:", student["name"])

# 3. Add a new key-value pair
student["city"] = "Delhi"
print("After adding:", student)

# 4. Update a value
student["age"] = 21
print("After updating:", student)

# 5. Delete a key-value pair
del student["course"]
print("After deleting:", student)

# 6. Get all keys
print("Keys:", student.keys())

# 7. Get all values
print("Values:", student.values())

# 8. Get all key-value pairs
print("Items:", student.items())

# 9. Check whether a key exists
print("name" in student)

# 10. Get the number of items
print("Length:", len(student))

# 11. Remove an item using pop()
student.pop("age")
print("After pop:", student)

# 12. Clear the dictionary
student.clear()
print("After clearing:", student)