from tkinter import *
from client_final import *


root = Tk()
root.title('Chat-App')
root.iconbitmap('D:\Python\Chat App\logo.ico')

canvas = Canvas(root, height = 200, width = 200)
canvas.grid(row=5,column=5)


myLabel1 = Label(root, text = (my_username + '>'))
myLabel1.grid(row = 0, column = 0)

e = Entry(root, width = 40)
e.grid(row = 0, column = 1)
e.insert(0, 'Enter Message here')
message = e.get

def myClick():

    myLabel2 = Label(root, text=message)
    myLabel2.grid(row=2, column=1)

myButton = Button(root, text = 'Send Message', command = myClick, width = 10)
myButton.grid(row = 0, column = 2)



root.mainloop()