def addstudent():
    def submitadd():
        
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")

        try:
            strr='insert into studentdata1 values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(strr,(id, name, mobile, email, address, gender, dob, addeddate,addedtime))
            con.commit()
            res=messagebox.askyesnocancel('Notifications', 'Id {} Name {} Added successfully... and want to clean the form'.format(id, name), parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
                
        except:
            messagebox.showerror('Notifications', 'Id Already Satisfied....', parent=addroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)


    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('450x470+30+150')
    addroot.title('Student Management System')
    addroot.config(bg='pink')

    


    idlabel=Label(addroot, text='Enter Id:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel=Label(addroot, text='Enter Name:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel=Label(addroot, text='Enter Mobile:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel=Label(addroot, text='Enter Email:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel=Label(addroot, text='Enter Address:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel=Label(addroot, text='Enter Gender:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel=Label(addroot, text='Enter D.O.B:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    doblabel.place(x=10, y=370)


    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    

    identry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry=Entry(addroot, font=('times', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=230, y=370)


    submitbtn=Button(addroot, text='SUBMIT', font=('times', 15, 'bold'), width=15, bd=5, bg='black', foreground='white', 
                    activebackground='lightgrey', activeforeground='black', command=submitadd)
    submitbtn.place(x=150, y=420)
    
    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(mobile != ''):
            strr = 'select *from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(dob != ''):
            strr = 'select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('450x560+30+100')
    searchroot.title('Student Management System')
    searchroot.config(bg='pink')


    idlabel=Label(searchroot, text='Enter Id:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel=Label(searchroot, text='Enter Name:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel=Label(searchroot, text='Enter Mobile:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel=Label(searchroot, text='Enter Email:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel=Label(searchroot, text='Enter Address:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel=Label(searchroot, text='Enter Gender:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot,text='Enter D.O.B : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(searchroot, text='Enter Date:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    datelabel.place(x=10, y=430)


    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval = StringVar()
    dateval=StringVar()
    

    identry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry=Entry(searchroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=230,y=370)

    dateentry=Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=230, y=430)


    submitbtn=Button(searchroot, text='SUBMIT', font=('times', 15, 'bold'), width=15, bd=5, bg='black', foreground='white', 
                    activebackground='lightgrey', activeforeground='black', command=search)
    submitbtn.place(x=150, y=490)
    
    searchroot.mainlopp()

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('450x590+30+40')
    updateroot.title('Student Management System')
    updateroot.config(bg='pink')


    idlabel=Label(updateroot, text='Enter Id:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel=Label(updateroot, text='Enter Name:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel=Label(updateroot, text='Enter Mobile:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel=Label(updateroot, text='Enter Email:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel=Label(updateroot, text='Enter Address:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel=Label(updateroot, text='Enter Gender:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot,text='Enter D.O.B : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date : ',bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=4,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot, text='Enter Time:- ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=4, width=12, anchor='w')
    timelabel.place(x=10, y=490)


    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval=StringVar()
    

    identry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=230, y=10)

    nameentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=230, y=70)

    mobileentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=230, y=130)

    emailentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=230, y=190)

    addressentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=230, y=250)

    genderentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=230, y=310)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=230,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=230,y=430)

    timeentry=Entry(updateroot, font=('times', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=230, y=490)


    submitbtn=Button(updateroot, text='SUBMIT', font=('times', 15, 'bold'), width=15, bd=5, bg='black', foreground='white', 
                    activebackground='lightgrey', activeforeground='black', command=update)
    submitbtn.place(x=150, y=540)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    
    updateroot.mainlopp()

def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def exitstudent():
    res=messagebox.askyesnocancel('Notification', 'Do you want to exit?')  
    if(res==True):
        root.destroy()



def Connectdb():
    def submitdb():
        global con, mycursor
        # host=hostval.get()
        # user=userval.get()
        # password=passwordval.get()
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        try:
            con=pymysql.connect(host=host, user=user, password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect pls try again', parent=dbroot)
            return
        try:
            strr='create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            strr='create table studentdata1(id Int , name varchar(23), mobile varchar(12), email varchar(34), address varchar(30), gender varchar(10), dob varchar(23), date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr='alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database Created and you are connected', parent=dbroot)
            

        except:
            strr='use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'You are connected with database', parent=dbroot)
        dbroot.destroy()
        
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+690+230')
    dbroot.config(bg='pink')



    hostlabel=Label(dbroot, text='Enter Host-: ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel=Label(dbroot, text='Enter User-: ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel=Label(dbroot, text='Enter Password-: ', bg='white', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)



    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()
    
    hostentry=Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry=Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry=Entry(dbroot, font=('times', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)


    submitbutton=Button(dbroot, text='Submit', font=('times', 15, 'bold'), bg='black', foreground='white', bd=5, width=18, activebackground='white', activeforeground='black' ,command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


def tick():
    date_string = time.strftime("%d/%m/%Y")
    time_string = time.strftime("%H:%M:%S")
    # date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)

from tkinter import*
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas 
import pymysql
import time
root=Tk()
root.config(bg='white')
root.geometry('1020x735+200+50')
root.title("STUDENT MANAGEMENT SYSTEM")

image_url ="https://www.google.com/url?sa=i&url=https%3A%2F%2Fpicjumbo.com%2Ffree-photos%2Fbackgrounds%2F&psig=AOvVaw1IZRiFIKoIfysr5FIZOAaM&ust=1730038444723000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPCo8s2drIkDFQAAAAAdAAAAABAJ"

DataEntryFrame=Frame(root, bg='black', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=550)



frontlabel=Label(DataEntryFrame, text='-------------WELCOME--------------', width=30, font=('arial', 22, 'italic bold'), bg='white')
frontlabel.pack(side=TOP, expand=True)


addbtn=Button(DataEntryFrame, text='1. Add Student', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=addstudent)
addbtn.pack(side=TOP, expand=True)

deletebtn=Button(DataEntryFrame, text='2. Delete Student', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn=Button(DataEntryFrame, text='3. Update Student', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

searchbtn=Button(DataEntryFrame, text='4. Search Student', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

showallbtn=Button(DataEntryFrame, text='5. Show All', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=showstudent)
showallbtn.pack(side=TOP, expand=True)

exitbtn=Button(DataEntryFrame, text='6. Exit', width=25, font=('times', 20, 'bold'), bd=5, bg='white', activebackground='pink', relief=RIDGE, activeforeground='black', command=exitstudent)
exitbtn.pack(side=TOP, expand=True)




ShowDataFrame=Frame(root, bg='black', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=600, y=80, width=670, height=550)


style=ttk.Style()
style.configure('Treeview.Heading', font=('times', 20, 'bold'))
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x=Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttable=Treeview(ShowDataFrame, columns=('Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date','Added Time'), 
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)     
scroll_y.pack(side=RIGHT, fill=Y)         
scroll_x.config(command=studenttable.xview)    
scroll_y.config(command=studenttable.yview)     
studenttable.heading('Id', text='Id') 
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile', text='Mobile')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('Id', width=100)
studenttable.column('Name', width=200)
studenttable.column('Mobile', width=200)
studenttable.column('Email', width=300)
studenttable.column('Address', width=200)
studenttable.column('Gender', width=100)
studenttable.column('D.O.B', width=150)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)
studenttable.pack(fill=BOTH, expand=1)

ss="STUDENT MANAGEMENT SYSTEM"
count=0
text=''



SliderLabel=Label(root, text=ss, font=('chiller', 30, 'italic bold'), relief=RIDGE, borderwidth=5, width=30, bg='white')
SliderLabel.place(x=260, y=0)


clock = Label(root,font=('times',15,'bold'),relief=RIDGE,borderwidth=4,bg='black', foreground='white', width=18)
clock.place(x=0,y=0)
tick()

connectbutton=Button(root, text='Connect To Database', width=20, font=('times', 15, 'bold'), relief=RIDGE, borderwidth=4, bg='black', foreground='white', 
                     activebackground='black', activeforeground='white', command=Connectdb)
connectbutton.place(x=1020, y=0)
root.mainloop()