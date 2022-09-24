
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
from linearregressionhouse import df2


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = Tk()
        self.title('Tkinter StringVar')
        self.geometry("600x200")

        self.name_var = tk.StringVar()

        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(2, weight=1)
        # self.columnconfigure(3, weight=1)
        # self.columnconfigure(4, weight=1)
        # self.columnconfigure(5, weight=1)
        # self.columnconfigure(6, weight=1)
        # self.columnconfigure(7, weight=1)
        # self.columnconfigure(8, weight=1)
        # self.columnconfigure(9, weight=1)


        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 1, 'pady': 1}
        # label
        floor = Label(self, text='Floor').grid(column=0, row=0, **padding)

        # Floor number
        floornumber = df2['floor level'].unique()
        floor_number = Listbox(self,width=5,height=5,selectmode=SINGLE)
        sb1=Scrollbar(self)
        sb1.grid(column=1,row=1)

        
        for i in range(len(floornumber)):

            floor_number.insert(i,f'{floornumber[i]}')

        floor_number.configure(yscrollcommand=sb1.set)
        sb1.configure(command=floor_number.yview)
        floor_number.grid(column=0, row=1, **padding)
        floor_number.focus()

        # List of HOuse
        titlebed = Label(self,text="Number of bedrooms")
        bedroom_number = Listbox(self, width=5,height=5, selectmode=SINGLE,yscrollcommand='YES')
        bedroomnumber  = df2['BHK'].unique()
        for i in range(len(bedroomnumber)):

            bedroom_number.insert(i,f'{bedroomnumber[i]}')
        

        # sb2=Scrollbar(self)
        # sb2.grid(column=4,row=1)
        # bedroom_number.configure(yscrollcommand=sb2.set)
        # sb2.configure(command=bedroom_number.yview)
        
        titlebed.grid(column=3,row=0,**padding)
        bedroom_number.grid(column=3,row=1,**padding)


        # Area Type
        areatypetitle = Label(self,text='Area Type')
        areatypes = Listbox(self, width=10,height=5,selectmode=SINGLE)
        area_types  = df2['Area Type'].unique()

        # area_types = ["Super Area", "Built Area", "Carpet Area"]
        for i in range(len(area_types)):
            areatypes.insert(i,f'{area_types[i]}')

        areatypetitle.grid(column=4,row=0,**padding)
        areatypes.grid(column=4,row=1,**padding)


        # City
        citytitle = Label(self,text='City')
        city = Listbox(self, width=10,height=5,selectmode=SINGLE)
        city_names  = df2['City'].unique()

        
        for i in range(len(city_names)):
            city.insert(i,f'{city_names[i]}')

        citytitle.grid(column=5,row=0,**padding)
        city.grid(column=5,row=1,**padding)

         # Furnishing Status
        furnishtitle = Label(self,text='Furnishing Status')
        furnishes = Listbox(self, width=10,height=5,selectmode=SINGLE)
        furnish_status  = df2['Furnishing Status'].unique()

        
        for i in range(len(furnish_status)):
            furnishes.insert(i,f'{furnish_status[i]}')

        furnishtitle.grid(column=6,row=0,**padding)
        furnishes.grid(column=6,row=1,**padding)

         # Tenant Pref
        Tenanttitle = Label(self,text='Tenant Preferred')
        preftenant = Listbox(self, width=15,height=5,selectmode=SINGLE)
        pref_tenant  = df2['Tenant Preferred'].unique()

        
        for i in range(len(pref_tenant)):
            preftenant.insert(i,f'{pref_tenant[i]}')

        Tenanttitle.grid(column=7,row=0,**padding)
        preftenant.grid(column=7,row=1,**padding)


         # Number of Bathroom
        bathroomtitle = Label(self,text='Number of Bathroom')
        bathroom = Listbox(self, width=5,height=5,selectmode=SINGLE)
        bathroom_number  = df2['Bathroom'].unique()

        
        for i in range(len(bathroom_number)):
            bathroom.insert(i,f'{bathroom_number[i]}')

        bathroomtitle.grid(column=8,row=0,**padding)
        bathroom.grid(column=8,row=1,**padding)










        
        # Button
        # submit_button = ttk.Button(self, text='Submit', command=self.submit)
        # submit_button.grid(column=5, row=1, **padding)

        # Output label
        self.output_label = ttk.Label(self)
        self.output_label.grid(column=8, row=1, columnspan=3, **padding)

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
