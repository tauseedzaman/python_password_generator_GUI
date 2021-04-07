from tkinter import *
from tkinter import messagebox
import pyperclip as PCP 
import string
import random

#create app
app = Tk()
#set window title
app.title("Password Generator")
#set window 
app.geometry('500x300+400+100')
#set background black
app.config(bg="black")

#function password generator
def generate():
	x = int(length.get())
	if x == '':
		messagebox.showinfo("Hai","Enter password length")
		return
	set = string.ascii_letters+string.digits+string.punctuation
	password=""
	for char in range(x):
		rand_char = random.choice(set)
		password = password + rand_char
	password_Box.delete(1.0,END)
	password_Box.insert(1.0,password)
#function for copying password
def copy():
	text = password_Box.get(1.0,END)
	PCP.copy(text)
# title
Label(app,text="Password Generator",bg="black",fg="red",font=("verdana ", 30,"bold")).place(x=50,y=20)
#password label
Label(app,text="Created Password**",bg="black",fg="cyan",font=("times bold ", 15)).place(x=50,y=100)
#password box
password_Box = Text(app,bg="black",fg="cyan",font=("times bold ", 30),bd=2,relief=GROOVE,width=17,height=1)
#length label
Label(app,text="Length",bg="black",fg="red",font=("times bold ", 15)).place(x=420,y=100)
#length entry
length = Entry(app,bg="black",fg="yellow",font=("times bold ", 30),bd=2,relief=GROOVE,width=2)
#generate password button
Button(app,text="Generate",bg="blue",fg="gold",font=("verdana", 20),command=generate,bd=2,relief=GROOVE,width=5,padx=20).place(x=50,y=200)
#copy password button
Button(app,text="Copy",bg="blue",fg="gold",font=("times", 20),command=copy,bd=2,relief=GROOVE,width=5,padx=10).place(x=370,y=200)
#bottom text label
Label(app,text="just enter password length\nAnd start hiting the generate button until you get your favorite password.",bg="black",fg="yellow",font=("verdana ", 10, "underline")).place(x=50,y=265)

length.place(x=430,y=130)
password_Box.place(x=50,y=130)
app.mainloop()


