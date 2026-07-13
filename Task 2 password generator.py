import random
import string
print("PASSWORD GENERATOR")
length = int(input("Enter password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "Priya verma"
for i in range(length):
    password += random.choice(characters)
print("Generated Password:", password)
