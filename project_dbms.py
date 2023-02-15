from tkinter import *
import tkinter.messagebox as box
import mysql.connector as mysql
import time

def conn():
    """connecting to the mysql server"""
    return mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "project"
)

book = Tk()    

def insert_record():
    check_counter = 0
    warn = ""
    if nameentry.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if emailentry.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if phoneentry.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if passwordentry.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if passwordcheckentry.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1
    
    if passwordentry.get() != passwordcheckentry.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 7:
        try:
            con = conn()
            cur = con.cursor()
            cur.execute("create table if not exists record(name char(20),email varchar(35) primary key,phone int,gender char(6),password varchar(20))")
            cur.execute(f"INSERT INTO record VALUES ('{nameentry.get()}',"
                        f"'{emailentry.get()}',"
                        f"{phoneentry.get()},"
                        f"'{var.get()}', "
                        f"'{passwordentry.get()}')"
            )
            con.commit()
            box.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            box.showerror('', ep)
    else:
        box.showerror('Error', warn)

def fetches():
    """displays the SQL table"""
    con = conn()
    cur = con.cursor() 
    cur.execute("SELECT * FROM record")
    i=5
    for k in cur:
        for j in range(len(k)):
            e = Entry(book,width = 12,bg = "#d0efb1",font="comicsansms 12")
            e.grid(row=i,column = j+1)
            e.insert(END, k[j])
            e=Label(book,width=12,text='Name',font="comicsansms 12",relief='ridge',anchor='w',bg="#74c69d")
            e.grid(row=4,column=1)
            e=Label(book,width=12,text='Email',font="comicsansms 12",relief='ridge',anchor='w',bg="#74c69d")
            e.grid(row=4,column=2)
            e=Label(book,width=12,text='phone',font="comicsansms 12",relief='ridge',anchor='w',bg="#74c69d")
            e.grid(row=4,column=3)
            e=Label(book,width=12,text='Gender',font="comicsansms 12",relief='ridge',anchor='w',bg="#74c69d")
            e.grid(row=4,column=4)
            e=Label(book,width=12,text='Password',font="comicsansms 12",relief='ridge',anchor='w',bg="#74c69d")
            e.grid(row=4,column=5)
        i=i+1
        

book.geometry("1200x700")
book.config(bg="#cfe8ef")
book.title("ITS A LOGIN PAGE")
Label(text = "Something and Everything",font="comicsansms 30 bold",bg = "#85c7de").grid(row = 1,column = 0,padx = 10,pady =10)
Label(text=time.asctime(),font="comicsansms 10 bold",bg = "#cfe8ef").grid(sticky = E)
name = Label(text = "Enter Name:",font = "comicsansms 15",bg="#cfe8ef")
email = Label(text = "Enter Email:",font = "comicsansms 15",bg="#cfe8ef")
gender = Label(text="Select Gender",bg='#cfe8ef',font="comicsansms 15")
phone = Label(text = "Enter contact:",font = "comicsansms 15",bg="#cfe8ef")
password = Label(text = "Create a password:",font = "comicsansms 15",bg="#cfe8ef")
passwordcheck = Label(text = "Confirm password:",font = "comicsansms 15",bg="#cfe8ef")

namevalue = StringVar()
emailvalue = StringVar()
passwordvalue = StringVar()
passwordcheckvalue = StringVar()

var = StringVar()
var.set('male')

nameentry = Entry(book,textvariable=namevalue)
emailentry = Entry(book,textvariable=emailvalue)
passwordentry = Entry(book,textvariable=passwordvalue)
passwordcheckentry = Entry(book,textvariable=passwordcheckvalue)
phoneentry = Entry(book)

nameentry.grid(row = 3, column = 0,padx = 10,pady = 8)
emailentry.grid(row = 4, column = 0,padx = 10,pady = 8)
phoneentry.grid(row = 5, column = 0,padx = 10,pady = 8)
passwordentry.grid(row = 7, column = 0,padx = 10,pady = 8)
passwordcheckentry.grid(row = 8, column = 0,padx = 10,pady = 8)

name.grid(row = 3, column = 0,padx = 10, sticky=W,pady = 8)
email.grid(row = 4, column = 0,padx = 10, sticky=W,pady = 8)
phone.grid(row = 5, column = 0,padx = 10, sticky=W,pady = 8)
password.grid(row = 7, column = 0,padx = 10, sticky=W,pady = 8)
passwordcheck.grid(row = 8, column = 0,padx = 10, sticky=W,pady = 8)
gender.grid(row=6, column=0, sticky=W,padx = 10, pady=10)

genders = Label()
male_rb = Radiobutton(genders,text='Male',bg='#52b788',variable=var,value='male',font="comicsansms 12",)
female_rb = Radiobutton(genders,text='Female',bg='#74c69d',variable=var,value='female',font="comicsansms 12",)
others_rb = Radiobutton(genders,text='Others',bg='#52b788',variable=var,value='others',font="comicsansms 12")

genders.grid(row=6, pady=10)
male_rb.pack (side=LEFT)
female_rb.pack(side=LEFT)
others_rb.pack(expand=True, side=LEFT)

submit = Button(text="Register",font="bold",bg = "#ea9ab2",command=insert_record)
submit.grid(column=0,padx = 20,pady=15)

submit1 = Button(text="Display Data",font="bold",bg = "#e27396",command=fetches)
submit1.grid(column = 0)

book.mainloop()
