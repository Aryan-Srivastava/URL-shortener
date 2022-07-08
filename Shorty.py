from tkinter import *
import pyshorteners

root = Tk()
root.title("URL Shortener")
root.geometry("500x500")

def shorten():
    if my_entry.get():
        url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
        shorty.insert(END, url)

my_label = Label(root, text="Enter a link to shorten:", font=("Helvetica", 16))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 16))
my_entry.pack(pady=20)

my_button = Button(root, text="shorten Link", font=("Helvetica", 16), command=shorten)
my_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link:", font=("Helvetica", 16))
shorty_label.pack(pady=20)

shorty = Entry(root, font=("Helvetica", 16), justify=CENTER, width=30, bd=0, bg="systembuttonface")
shorty.pack(pady=20)

root.mainloop()