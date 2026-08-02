from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# -------------------------
# Load Secret Key
# -------------------------
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

PASSWORD = "1234"

# -------------------------
# Login Function
# -------------------------
def check_login():
    if password_entry.get() == PASSWORD:
        login.destroy()
        open_main_window()
    else:
        messagebox.showerror("Error", "Incorrect Password")


# -------------------------
# Main Window
# -------------------------
def open_main_window():
    window = Tk()
    window.title("Secure File Encryption System")
    window.geometry("500x350")
    window.resizable(False, False)

    title = Label(
        window,
        text="Secure File Encryption & Decryption",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=20)

    # -------------------------
    # Encrypt Function
    # -------------------------
    def encrypt_file():
        file_path = filedialog.askopenfilename()

        if file_path == "":
            return

        try:
            with open(file_path, "rb") as file:
                data = file.read()

            encrypted = cipher.encrypt(data)

            with open(file_path, "wb") as file:
                file.write(encrypted)

            messagebox.showinfo("Success", "File Encrypted Successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -------------------------
    # Decrypt Function
    # -------------------------
    def decrypt_file():
        file_path = filedialog.askopenfilename()

        if file_path == "":
            return

        try:
            with open(file_path, "rb") as file:
                data = file.read()

            decrypted = cipher.decrypt(data)

            with open(file_path, "wb") as file:
                file.write(decrypted)

            messagebox.showinfo("Success", "File Decrypted Successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    Button(
        window,
        text="Encrypt File",
        font=("Arial", 14),
        width=20,
        command=encrypt_file
    ).pack(pady=10)

    Button(
        window,
        text="Decrypt File",
        font=("Arial", 14),
        width=20,
        command=decrypt_file
    ).pack(pady=10)

    Button(
        window,
        text="Exit",
        font=("Arial", 14),
        width=20,
        command=window.destroy
    ).pack(pady=10)

    window.mainloop()


# -------------------------
# Login Window
# -------------------------
login = Tk()
login.title("Login")
login.geometry("300x180")
login.resizable(False, False)

Label(
    login,
    text="Secure File Encryption",
    font=("Arial", 14, "bold")
).pack(pady=10)

Label(login, text="Enter Password").pack()

password_entry = Entry(login, show="*", width=25)
password_entry.pack(pady=5)

Button(
    login,
    text="Login",
    command=check_login
).pack(pady=10)

login.mainloop()