from tkinter import *
from tkinter import messagebox
import os

win = Tk()
win.title('Verify')
win.geometry('350x200')
win.resizable(width=False,height=False)

root = Toplevel(win)
root.title('Login')
root.withdraw()
root.geometry('350x150')
root.resizable(width=False,height=False)

top = Toplevel(root)
top.title('Email Storage')
top.withdraw()
top.geometry('550x360')
top.resizable(width=False,height=False)

title = Label(win,text='password verify:--',font=('times new romann',15))
title.grid(row=0,column=0)
title.configure(foreground='blue')

def confirm():
	list1 = []
	v1 = entry1.get()
	v2 = entry2.get()

	if v1 == v2 and v1 == v2 != '':
		with open('pass.txt','w') as f:
			list1.append(v2)
			print(list1)
			f.writelines(v2)
			f.close()
		entry1.delete(0,END)
		entry2.delete(0,END)
		msg = messagebox.showinfo('Congrates','Now you access to this system')
	else:
		msg = messagebox.showerror('Error','Password does not match ! enter matching password')
		entry1.delete(0,END)
		entry2.delete(0,END)

def login():
	msg = messagebox.askyesno('security','Have you created your password')
	if msg is True:
		root.deiconify()	
	else:
		return False
				
attempts = 0
def login1():
	global attempts
	password = entry3.get()
	f = open('pass.txt','r')
	data = f.readlines()
	for password1 in data:
		if password == password1:
			entry3.delete(0,END)
			top.deiconify()
		else:
			attempts += 1
			if attempts == 5:
				win.destroy()
			entry3.delete(0,END)
			msg = messagebox.askretrycancel('warning','wrong password attempts left-->' + str(5 - attempts))
			if msg is True:
				return root	

def add1():
	entry4.get()
	entry5.get()
	entry6.get()
	entry7.get()
	txt.insert(END,'Name\t\t' + 'Email\t\t' + 'Password\t\t\n\n')
	txt.insert(END,str(entry4.get()) +'\t\t' + str(entry5.get()) + '\t\t' + str(entry6.get()) + '\n')
	entry4.delete(0,END)
	entry5.delete(0,END)
	entry6.delete(0,END)
	entry7.delete(0,END)

def delete1():
	txt.delete(1.0,END)
	
lbl1 = Label(win,text='password:--',font=('times new romann',12))
lbl1.grid(row=1,column=0,pady=7,sticky=W)

lbl2 = Label(win,text='confirm password:--',font=('times new romann',12))
lbl2.grid(row=2,column=0,pady=7,sticky=W)

entry1 = Entry(win,width=15,show='*',font=('times new roman',15))
entry1.grid(row=1,column=1,padx=10)

entry2 = Entry(win,width=15,show='*',font=('times new roman',15))
entry2.grid(row=2,column=1,padx=10)

btn1 = Button(win,width=13,height=3,text='Verify',command=confirm)
btn1.grid(row=3,pady=30,sticky=W)

btn2 = Button(win,width=13,height=3,text='Login',command=login)
btn2.grid(row=3,column=1,pady=30,sticky=E)

title1 = Label(root,text='Login:--',font=('times new romann',15))
title1.grid(row=0,column=0,sticky=W)
title1.configure(foreground='blue')

lbl3 = Label(root,text='Enter password:--',font=('times new romann',12))
lbl3.grid(row=2,column=0,pady=7,sticky=W)

entry3 = Entry(root,width=15,show='*',font=('times new roman',15))
entry3.grid(row=2,column=1,padx=10)

btn3 = Button(root,width=13,height=3,text='Login',command=login1)
btn3.grid(row=3,column=1,pady=25,sticky=W)

lbl4 = Label(top,text='Name:--',font=('times new romann',12))
lbl4.grid(row=0,column=0,pady=7,sticky=W)

lbl5 = Label(top,text='Email:--',font=('times new romann',12))
lbl5.grid(row=0,column=2,pady=7,sticky=W)

lbl6 = Label(top,text='password:--',font=('times new romann',12))
lbl6.grid(row=1,column=0,pady=7,sticky=W)

lbl7 = Label(top,text='Mobile no:--',font=('times new romann',12))
lbl7.grid(row=1,column=2,pady=7,sticky=W)

entry4 = Entry(top,width=15,font=('times new roman',15))
entry4.grid(row=0,column=1)

entry5 = Entry(top,width=15,font=('times new roman',15))
entry5.grid(row=0,column=3,padx=10)

entry6 = Entry(top,width=15,font=('times new roman',15))
entry6.grid(row=1,column=1,padx=10)

entry7 = Entry(top,width=15,font=('times new roman',15))
entry7.grid(row=1,column=3,padx=10)

btn3 = Button(top,width=13,height=2,text='Add',command=add1)
btn3.grid(row=3,column=1,pady=20,sticky=W)

btn4 = Button(top,width=13,height=2,text='Clear',command=delete1)
btn4.grid(row=3,column=3,pady=20,sticky=W)

frm = Frame(top,bd=4,relief='sunken')
frm.place(x=5,y=145,height=200,width=540)

txt = Text(frm,width=66,height=13,font=('times new roman',15),state='normal')
scrl = Scrollbar(frm)
scrl.pack(side=RIGHT,fill=Y)
txt.pack(fill=BOTH,expand=True)
scrl.config(command=txt.yview)
txt.config(yscrollcommand=scrl.set)

win.mainloop()