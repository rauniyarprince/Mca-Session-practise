# Program to demonstrate contact dictionary operations

contacts = {
    "Rahul": "9876543210",
    "Priya": "9876501234",
    "Amit": "9876512345"
}

print("Original Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)

# Add contact
contacts["Neha"] = "9876523456"

# Update contact
contacts["Rahul"] = "9999999999"

# Delete contact
del contacts["Amit"]

# Search contact
search_name = "Priya"

if search_name in contacts:
    print("\nContact Found:")
    print(search_name, ":", contacts[search_name])
else:
    print("\nContact not found")

# Display all contacts
print("\nAll Contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)