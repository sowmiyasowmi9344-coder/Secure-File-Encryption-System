from cryptography.fernet import Fernet

# Load the secret key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Ask the user for the file name
filename = input("Enter file name to decrypt: ")

# Read the encrypted file
with open(filename, "rb") as file:
    encrypted_data = file.read()

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

# Write the original data back to the file
with open(filename, "wb") as file:
    file.write(decrypted_data)

print("✅ File Decrypted Successfully!")