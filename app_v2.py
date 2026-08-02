from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os
print("Program Started")

# Load encryption key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)


PASSWORD = "1234"
selected_file = ""


# Encrypt Function
def encrypt_file():

    if selected_file == "":
        messagebox.showwarning(
            "Warning",
            "Please select a file first"
        )
        return

    try:
        with open(selected_file, "rb") as file:
            data = file.read()

        encrypted_data = cipher.encrypt(data)

        folder = os.path.dirname(selected_file)

        filename = os.path.splitext(
            os.path.basename(selected_file)
        )[0]

        encrypted_file = os.path.join(
            folder,
            filename + "_encrypted.enc"
        )

        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo(
            "Success",
            "File Encrypted Successfully"
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            str(e)
        )


# Decrypt Function
def decrypt_file():

    if selected_file == "":
        messagebox.showwarning(
            "Warning",
            "Please select an encrypted file first"
        )
        return

    try:
        with open(selected_file, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = cipher.decrypt(encrypted_data)

        folder = os.path.dirname(selected_file)

        decrypted_file = os.path.join(
            folder,
            "decrypted_file.txt"
        )

        with open(decrypted_file, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo(
            "Success",
            "File Decrypted Successfully"
        )

    except:
        messagebox.showerror(
            "Error",
            "Invalid encrypted file"
        )


# Main Window
def open_main_window():

    global selected_file

    window = Tk()

    window.title(
        "Secure File Encryption System"
    )

    window.geometry(
        "600x450"
    )

    window.resizable(
        False,
        False
    )


    Label(
        window,
        text="🔐 Secure File Encryption & Decryption",
        font=("Arial",18,"bold")
    ).pack(pady=30)


    file_label = Label(
        window,
        text="No File Selected",
        fg="blue",
        font=("Arial",10)
    )

    file_label.pack()


    def browse_file():

        global selected_file

        selected_file = filedialog.askopenfilename()

        if selected_file:
            file_label.config(
                text=selected_file
            )


    Button(
        window,
        text="📂 Browse File",
        width=20,
        font=("Arial",14),
        command=browse_file
    ).pack(pady=15)


    Button(
        window,
        text="🔒 Encrypt File",
        width=20,
        font=("Arial",14),
        command=encrypt_file
    ).pack(pady=10)


    Button(
        window,
        text="🔓 Decrypt File",
        width=20,
        font=("Arial",14),
        command=decrypt_file
    ).pack(pady=10)


    Button(
        window,
        text="❌ Exit",
        width=20,
        font=("Arial",14),
        command=window.destroy
    ).pack(pady=10)


    window.mainloop()



# Login Function
def check_login():

    if password_entry.get() == PASSWORD:

        login.destroy()

        open_main_window()

    else:

        messagebox.showerror(
            "Error",
            "Wrong Password"
        )



# Login Window

login = Tk()

login.title(
    "Login"
)

login.geometry(
    "350x250"
)

login.resizable(
    False,
    False
)


Label(
    login,
    text="Secure File Encryption",
    font=("Arial",16,"bold")
).pack(pady=30)


Label(
    login,
    text="Enter Password"
).pack()


password_entry = Entry(
    login,
    show="*",
    width=25
)

password_entry.pack(pady=10)


Button(
    login,
    text="Login",
    width=15,
    command=check_login
).pack(pady=10)


login.mainloop()