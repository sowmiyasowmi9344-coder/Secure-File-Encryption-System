from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Ask the user for the file name
filename = input("Enter file name to encrypt: ")

# Read the file
with open(filename, "rb") as file:
    file_data = file.read()

# Encrypt the data
encrypted_data = cipher.encrypt(file_data)

# Write the encrypted data back to the file
with open(filename, "wb") as file:
    file.write(encrypted_data)

print("✅ File Encrypted Successfully!")