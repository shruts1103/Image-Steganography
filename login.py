from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+100+100')
root.configure(bg="#87CEEB")
root.resizable(False, False)

def on_button_click():
    root.destroy()  
    import window

def signin():
    username = user.get()
    password = code.get()

    if not username or not password:
        messagebox.showerror("Invalid", "Please enter a username and password")
        
    
    elif username == 'admin' and password == '1234':
        on_button_click()
      
    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "invalid username and password")

    elif password != "1234":
        messagebox.showerror("Invalid", "invalid password")

    elif username != 'admin':
        messagebox.showerror("Invalid", "invalid password")

#icon
image_icon = PhotoImage(file="loginpage.png")
root.iconphoto(False, image_icon) 


img = PhotoImage(file='background2.png')
Label(root, image=img, bg='white').place(x=20, y=75)

frame = Frame(root, width=350, height=280, bg="white")
frame.place(x=500, y=80)

heading = Label(frame, text='Sign in', fg='#57a1f8', font=('Times New Roman', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(frame, width=25, fg='black', border=0, font=('Times New Roman', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0,'Password')

code = Entry(frame, width=25, fg='black', border=0, font=('Times New Roman', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame,width=39, pady=10,text='Sign in',bg='#57a1f8', fg='white',border=0,command=lambda:(signin()) ).place(x=35,y=204)
         
root.mainloop()

