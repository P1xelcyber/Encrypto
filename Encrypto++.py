#GITHUB:P1xelcyber
from cryptography.fernet import Fernet
from tkinter import filedialog as fd
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import tkinter.messagebox 
import os
import base64


root = tk.Tk()
entry = Entry(root,width=45)
entry1 = Entry(root, width=45)

def generate_key():
    key1 = Fernet.generate_key()
    entry.config(foreground='black')
    entry.delete(0, 'end')
    entry.insert(0, key1)

def decrypt():
    path = entry1.get()
    key = entry.get()
    f = Fernet(key)
    if os.path.isfile(path):
        with open(path, "rb") as file:
            content = file.read()
        decrypted_content = f.decrypt(content)
        with open(path, "wb") as file:
            file.write(decrypted_content)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                patho = os.path.join(root, file)
                with open(patho, "rb") as file:
                    content = file.read()
                decrypted_content = f.decrypt(content)
                with open(patho, "wb") as file:
                    file.write(decrypted_content)

    else:
        tkinter.messagebox.showinfo("Error",  "Error code 342\nError fixes on github:p1xelcyber") 

def encrypt():
    path = entry1.get()
    key = entry.get()
    f = Fernet(key)
    if os.path.isfile(path):
        with open(path, "rb") as file:
            content = file.read()
        encrypted_content = f.encrypt(content)
        with open(path, "wb") as file:
            file.write(encrypted_content)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                patho = os.path.join(root, file)
                with open(patho, "rb") as file:
                    content = file.read()
                encrypted_content = f.encrypt(content)
                with open(patho, "wb") as file:
                    file.write(encrypted_content)
    else:
        tkinter.messagebox.showinfo("Error",  "Error code 342\nError fixes on github:p1xelcyber") 

def folder_path():
    fp3 = filedialog.askdirectory()
    entry1.config(foreground='black')
    entry1.delete(0, 'end')
    entry1.insert(0, fp3)

def file_path():
    fp2 = filedialog.askopenfilename()
    entry1.config(foreground='black')
    entry1.delete(0, 'end')
    entry1.insert(0, fp2)

def Load_key():
    entry.config(foreground='black')
    fp = filedialog.askopenfilename()
    with open(fp, "rb") as file:
        key = file.read().decode('utf-8')
    entry.delete(0, 'end')
    entry.insert(0, key)

def save_key():
    key = entry.get().encode('utf-8')
    with open("key.key", "wb") as file:
        file.write(key)
    tkinter.messagebox.showinfo("successful!",  "Key is saved to key.key") 

def on_entry_click(event):
    if entry.get() == 'Enter your key or generate one...':
       entry.delete(0, "end")
       entry.insert(0, '')
       entry.config(fg = 'black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your key or generate one...')
        entry.config(fg = 'grey')

#GITHUB:P1xelcyber
def on_entry_click1(event):
    if entry1.get() == 'Enter your key or generate one...':
       entry1.delete(0, 'end')
       entry1.insert(0, '')
       entry1.config(fg = 'black')

def on_focusout1(event):
    if entry1.get() == '':
        entry1.insert(0, 'Enter your key or generate one...')
        entry1.config(fg = 'grey')


root.title("Encrypto++")
root.geometry("700x300")
root.resizable(False, False)
icon = PhotoImage(file='Img/icon.png')
root.iconphoto(False, icon)

image = PhotoImage(file='Img/label.png') 
image2 = PhotoImage(file='Img/dice.png')
image3 = PhotoImage(file='Img/folder.png')
image4 = PhotoImage(file='Img/file.png')

label = tk.Label(text="Encrypto++", borderwidth=0)
label.config(font=("handjet", 40))
label.place(x=10, y=0)

label2 = Label(root, image = image)
label2.place(x=450,y=10)


entry.config(fg='grey')
entry.insert(0, 'Enter your key or generate one...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.place(x=25, y=80)

entry1.config(fg='grey')
entry1.insert(0, 'Select a path or a directory')
entry1.bind('<FocusIn>', on_entry_click1)  # Add this line to bind the FocusIn event
entry1.bind('<FocusOut>', on_focusout1)  # Add this line to bind the FocusOut event
entry1.place(x=25, y=170)
entry1.place(x=25, y=170)

button = Button(root, image=image2, command=generate_key)
button.place(x=395, y=80)

button1 = Button(root, text='Load Key',command=Load_key)
button1.place(x=25, y=108)

button2 = Button(root, text='Save Key',command=save_key)
button2.place(x=111, y=108)

button3 = Button(root, image=image3, command=folder_path)
button3.place(x=25, y=198)

button4 = Button(root, image=image4, command=file_path)
button4.place(x=83, y=198)

button5 = Button(root, command=encrypt, text='Encrypt')
button5.place(x=315, y=198)

button6 = Button(root, command=decrypt, text='Decrypt')
button6.place(x=315, y=233)

root.mainloop()
#GITHUB:P1xelcyber
