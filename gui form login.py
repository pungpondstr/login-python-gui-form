import mysql.connector
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="test"
)

def condition():
    username = ment1.get()
    password = ment2.get()

    mycursor = mydb.cursor()

    sql = "select * from member where Username = %s and Password = %s"

    var = (username, password)

    mycursor.execute(sql, var)

    myresult = mycursor.fetchone()

    if myresult:
        messagebox.showinfo('OK', 'Welcome : {}'.format(username))
    elif username == '' or password == '':
        messagebox.showerror('ERROR', 'Please Enter Username or Password')
    else:
        messagebox.showerror('ERROR', 'Username or Password wrong')
gui = Tk()

ment1 = StringVar()
ment2 = StringVar()
ment3 = StringVar()

gui.title('Login PointBlank TH')

gui.geometry('450x200')

l1 = Label(text='Username', font=14).pack()

textbox1 = Entry(textvariable=ment1, font=14).pack()

l2 = Label(text='Password', font=14).pack()

textbox2 = Entry(textvariable=ment2, show='*', font=14).pack()

l3 = Label(textvariable=ment3).pack()

button1 = Button(text='Login', command=condition, font=14, width=20).pack()

if __name__ == '__main__':
    gui.mainloop()
