from tkinter import *

window= Tk()

title_text = StringVar()
l1 = Label(window, text="Title")
l1.grid(row=0,column=0)

author_text = StringVar()
l2 = Label(window, text="Author")
l2.grid(row=0,column=2)

year_text = StringVar()
l3 = Label(window, text="Year")
l3.grid(row=1,column=0)

ISBN_text = StringVar()
l4 = Label(window, text="ISBN")
l4.grid(row=1,column=2)


# l2 = Label(window, text="Author")
# l1.grid(row=1,column=2)

title_text=StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4 = Entry(window, textvariable=ISBN_text)
e4.grid(row=1,column=3)

list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0, rowspan=8,columnspan=1)

sb1=Scrollbar(window)
sb1.grid(row=1,column=3)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window,text="View all", width=12)
b1.grid(row=2,column=2)




window.mainloop()