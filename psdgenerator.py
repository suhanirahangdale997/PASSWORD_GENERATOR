import random
import string

# Step 1: Take input from user
length = int(input("Enter password length: "))

# Step 2: Create character pool
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Step 4: Display password
print("Generated Password:", password)