
'''
Number of Bedrooms              0
Size                 0
Area Type            0
City                 0
Furnishing Status    0
Tenant Preferred     0
Number of Bathroom             0
Point of Contact     0
Date
dtype: int64
'''
# window= Tk()

import tkinter as tk
from tkinter import MULTIPLE, SINGLE,  ttk, Label, Entry, Listbox, Scrollbar
from tkinter.messagebox import YES
from tokenize import Single


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = Tk()
        self.title('Tkinter StringVar')
        self.geometry("600x200")

        self.name_var = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=1)
        self.columnconfigure(7, weight=1)
        self.columnconfigure(8, weight=1)
        self.columnconfigure(9, weight=1)


        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 1, 'pady': 1}
        # label
        floor = Label(self, text='Floor').grid(column=0, row=0, **padding)

        # Entry
        floornumber = range(-2,50)
        floor_number = Listbox(self,width=5,height=5,selectmode=SINGLE)
        sb1=Scrollbar(self)
        sb1.grid(column=1,row=1)

        
        for i in floornumber:

            floor_number.insert(i,'{}'.format(i))

        floor_number.configure(yscrollcommand=sb1.set)
        sb1.configure(command=floor_number.yview)
        floor_number.grid(column=0, row=1, **padding)
        floor_number.focus()

        # List of HOuse
        titlebed = Label(self,text="Number of bedrooms")
        bedroom_number = Listbox(self, width=5,height=5, selectmode=SINGLE,yscrollcommand='YES')

        bedroom_number.insert(1,'1')
        bedroom_number.insert(2,'2')
        bedroom_number.insert(3,'3')
        bedroom_number.insert(4,'4')
        bedroom_number.insert(5,'5')

        # sb2=Scrollbar(self)
        # sb2.grid(column=4,row=1)
        # bedroom_number.configure(yscrollcommand=sb2.set)
        # sb2.configure(command=bedroom_number.yview)
        
        titlebed.grid(column=3,row=0,**padding)
        bedroom_number.grid(column=3,row=1,**padding)

        
        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=5, row=1, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=5, row=1, columnspan=3, **padding)

#     def selected_item():
     
#     # Traverse the tuple returned by
#     # curselection method and print
#     # corresponding value(s) in the listbox
#         for i in listbox.curselection():
#             print(listbox.get(i))
 
# # Create a button widget and
# # map the command parameter to
# # selected_item function
# btn = Button(self, text='Print Selected', command=selected_item)
 
# # Placing the button and listbox
# btn.pack(side='bottom')
# listbox.pack()


    def submit(self):
        self.output_label.config(text=self.name_var.get())


if __name__ == "__main__":
    app = App()
    app.mainloop()

# title_text = StringVar()
# l1 = Label(window, text="Title")
# l1.grid(row=0,column=0)

# author_text = StringVar()
# l2 = Label(window, text="Author")
# l2.grid(row=0,column=2)

# year_text = StringVar()
# l3 = Label(window, text="Year")
# l3.grid(row=1,column=0)

# ISBN_text = StringVar()
# l4 = Label(window, text="ISBN")
# l4.grid(row=1,column=2)


# # l2 = Label(window, text="Author")
# # l1.grid(row=1,column=2)

# title_text=StringVar()
# e1 = Entry(window, textvariable=title_text)
# e1.grid(row=0,column=1)

# author_text=StringVar()
# e2 = Entry(window, textvariable=author_text)
# e2.grid(row=0,column=3)

# year_text=StringVar()
# e3 = Entry(window, textvariable=year_text)
# e3.grid(row=1,column=1)

# ISBN_text=StringVar()
# e4 = Entry(window, textvariable=ISBN_text)
# e4.grid(row=1,column=3)

# list1=Listbox(window, height=6,width=35)
# list1.grid(row=2,column=0, rowspan=8,columnspan=1)

# sb1=Scrollbar(window)
# sb1.grid(row=5,column=2)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)


# b1=Button(window,text="View all", width=12)
# b1.grid(row=2,column=3)

# b2=Button(window,text="Search Entry", width=12)
# b2.grid(row=3,column=3)

# b3=Button(window,text="Add Entry", width=12)
# b3.grid(row=4,column=3)

# b4=Button(window,text="Update selected", width=12)
# b4.grid(row=5,column=3)

# b4=Button(window,text="Delete selected", width=12)
# b4.grid(row=6,column=3)


# b5=Button(window,text="Delete selected", width=12)
# b5.grid(row=7,column=3)




# window.mainloop()