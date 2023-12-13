from tkinter import filedialog as fd
import tkinter as tk
from tkinter import *
from cryptography.fernet import Fernet
import os
from tkinter import filedialog


root = Tk()
root.title("Encrypto++")
root.geometry("670x400")
root.resizable(False, False)
root.configure(bg="black")
img = PhotoImage(file="hm2.png", )
Label(
    root,
    image=img,
    borderwidth=0
).place(x=450, y=-10)


key_entry = tk.Entry(root,bg="grey", fg="green",width="50")
key_entry.place(x=35, y=150)

def select_key():
    fp = fd.askopenfilename()
    with open(fp, "rb") as file:
        key = file.read().decode('utf-8')
    key_entry.delete(0, "end")
    key_entry.insert(0, key)

def path_selection():
    fp2 = filedialog.askdirectory()
    files = []
    for file in os.listdir(fp2):
        if file == "Encrypto++.py":
            continue
        files.append(file)
    label4.config(text=files)

def folder_path_selection():
    fp2 = filedialog.askdirectory()
    label4.config(text=fp2, fg="green")
    
def file_path_selection():
    fp3 = fd.askopenfilename()
    label4.config(fg="green", text=fp3)

def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0,"end")
    key_entry.insert(0,key)


def save_key_to_file():
    key = key_entry.get().encode('utf-8')
    with open("file.key", "wb") as file:
        file.write(key)


def encrypt():
    file_path = label4.cget("text")
    with open(file_path, 'rb') as file:
        original = file.read()

    key = key_entry.get()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)

    with open(file_path, 'wb') as file:
        file.write(encrypted)

def dencrypt():
    file_path = label4.cget("text")
    with open(file_path, 'rb') as file:
        original = file.read()

    key = key_entry.get()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(original)

    with open(file_path, 'wb') as file:
        file.write(decrypted)


load_button = tk.Button(root, text="Load Key", command=select_key, state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
load_button.place(x=359, y=180)

decrypt_button = tk.Button(root, text="Decrypt", command=dencrypt, state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
decrypt_button.place(x=365, y=310)

save_button = tk.Button(root, command=save_key_to_file,text="Save Key", state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
save_button.place(x=270, y=180)

save_button = tk.Button(root, command=encrypt,text="Encrypt", state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
save_button.place(x=284, y=310)

save_button2 = tk.Button(root,command=file_path_selection,text="Select file", state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
save_button2.place(x=35, y=310)

file_button2 = tk.Button(root,command=folder_path_selection,text="Select folder", state="normal", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green")
file_button2.place(x=131, y=310)

label = tk.Label(text="Encrypto++", foreground="green", bg="black", borderwidth=0)
label.config(font=("handjet", 50))
label.place(x=30, y=0)

label2 = tk.Label(text="Key⇩", foreground="green", bg="black", borderwidth=0)
label2.config(font=("handjet", 25))
label2.place(x=35, y=95)

label3 = tk.Label(text="Path⇩", foreground="green", bg="black", borderwidth=0)
label3.config(font=("handjet", 25))
label3.place(x=35, y=210)

label4 = tk.Label(foreground="green", bg="black", borderwidth=0)
label4.config(font=("handjet", 15))
label4.place(x=35, y=260)



def button_clicked():
    generate_key()

button = tk.Button(text="Generate key", borderwidth=0, bg="black", fg="green", activebackground='#2e2e2e', activeforeground="green", command=button_clicked)
button.place(x=35, y=180)





root.mainloop()
