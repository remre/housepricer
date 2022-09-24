
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
from tkinter import EXTENDED, MULTIPLE, SINGLE,  ttk, Label, Entry, Listbox, Scrollbar
from tkinter.messagebox import YES
from tokenize import Single
from turtle import width
from linearregressionhouse import df2


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = Tk()
        self.title('House Price Prediction Tool')
        self.geometry("600x200")

        self.name_var = tk.StringVar()
        # self.floor_number = Listbox(self,width=5,height=5,selectmode=SINGLE,exportselection=0)
        self.floor_number = ttk.Combobox(self,width=5)
        self.bedroom_number = ttk.Combobox(self,width=5)
        self.areatypes = ttk.Combobox(self,width=15)
        self.city = ttk.Combobox(self,width=10)
        
        self.furnishes = ttk.Combobox(self,width=15)
        self.preftenat = ttk.Combobox(self,width=15)
        self.bathroom = ttk.Combobox(self,width=5)
        
        # floor_number = self.floor_number

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
        floornumber =  list(sorted(df2['floor level'].unique()))
        # floor_number = Listbox(self,width=5,height=5,selectmode=SINGLE)
        # sb1=Scrollbar(self)
        # sb1.grid(column=1,row=1)

        
        # for i in range(len(floornumber)):

        #     self.floor_number.insert(i,f'{floornumber[i]}')
        self.floor_number['values'] = floornumber

        # self.floor_number.configure(yscrollcommand=sb1.set)
        # sb1.configure(command=self.floor_number.yview)
        self.floor_number.grid(column=0, row=1, **padding)
        self.floor_number.current(0)
        # self.floor_number.focus()

        # List of HOuse
        titlebed = Label(self,text="Number of bedrooms")
        # bedroom_number = Listbox(self, width=5,height=5, selectmode=SINGLE,exportselection=0)
        bedroomnumber  =  list(sorted(df2['BHK'].unique()))
        self.bedroom_number['values'] = bedroomnumber
        # for i in range(len(bedroomnumber)):

        #     bedroom_number.insert(i,f'{bedroomnumber[i]}')
        

        # sb2=Scrollbar(self)
        # sb2.grid(column=4,row=1)
        # bedroom_number.configure(yscrollcommand=sb2.set)
        # sb2.configure(command=bedroom_number.yview)
        
        titlebed.grid(column=3,row=0,**padding)
        self.bedroom_number.grid(column=3,row=1,**padding)
        self.bedroom_number.current(0)

        # Area Type
        areatypetitle = Label(self,text='Area Type')
        # areatypes = Listbox(self, width=10,height=5,selectmode=SINGLE,exportselection=0)
        area_types  =  list(sorted(df2['Area Type'].unique()))
        self.areatypes['values'] = area_types
        # area_types = ["Super Area", "Built Area", "Carpet Area"]
        # for i in range(len(area_types)):
        #     areatypes.insert(i,f'{area_types[i]}')

        areatypetitle.grid(column=4,row=0,**padding)
        self.areatypes.grid(column=4,row=1,**padding)
        self.areatypes.current(0)

        # City
        citytitle = Label(self,text='City')
        # city = Listbox(self, width=10,height=5,selectmode=SINGLE,exportselection=0)
        city_names  = list(sorted(df2['City'].unique()))
        self.city['values'] = city_names
        
        # for i in range(len(city_names)):
        #     city.insert(i,f'{city_names[i]}')

        citytitle.grid(column=5,row=0,**padding)
        self.city.grid(column=5,row=1,**padding)
        self.city.current(0)

         # Furnishing Status
        furnishtitle = Label(self,text='Furnishing Status')
        # furnishes = Listbox(self, width=10,height=5,selectmode=SINGLE,exportselection=0)
        self.furnishes['values']  =  list(sorted(df2['Furnishing Status'].unique()))

        
        # for i in range(len(furnish_status)):
        #     furnishes.insert(i,f'{furnish_status[i]}')

        furnishtitle.grid(column=6,row=0,**padding)
        self.furnishes.grid(column=6,row=1,**padding)
        self.furnishes.current(0)
         # Tenant Pref
        Tenanttitle = Label(self,text='Tenant Preferred')
        # preftenant = Listbox(self, width=15,height=5,selectmode=SINGLE,exportselection=0)
        pref_tenant  = list(sorted(df2['Tenant Preferred'].unique()))
        self.preftenat['values'] = pref_tenant
        
        # for i in range(len(pref_tenant)):
        #     preftenant.insert(i,f'{pref_tenant[i]}')

        Tenanttitle.grid(column=7,row=0,**padding)
        self.preftenat.grid(column=7,row=1,**padding)
        self.preftenat.current(0)

         # Number of Bathroom
        bathroomtitle = Label(self,text='Number of Bathroom')
        # bathroom = Listbox(self, width=5,height=5,selectmode=SINGLE,exportselection=0)
        bathroom_number  = list(sorted(df2['Bathroom'].unique()))
        self.bathroom['values'] = bathroom_number
        
        # for i in range(len(bathroom_number)):
        #     bathroom.insert(i,f'{bathroom_number[i]}')

        bathroomtitle.grid(column=8,row=0,**padding)
        self.bathroom.grid(column=8,row=1,**padding)
        self.bathroom.current(0)









        
        # Button
        submit_button = ttk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=9, row=1, **padding)

        # Output label
        rent = 500
        self.output_label = ttk.Label(self,text='Select features above and see the predicted rent that you gonna pay!!')
        self.output_label.grid(column=0, row=9, columnspan=15,rowspan=5, **padding)



    def submit(self):
        # for i in self.floor_number.curselection():
            answer_set = {
                            'Tenant Preferred': self.preftenat.get(),
                            'Number of Bedrooms': self.bedroom_number.get(),
                            'Floor': self.floor_number.get(),
                            'Area Type': self.areatypes.get(),
                            'City': self.city.get(),
                            'Furnishes': self.furnishes.get(),
                            'Bathrooms':self.bathroom.get()
            }

            # for i in answer_set:
            # self.output_label.config(text=answer_set.values())
            rent = 500
            self.output_label.config(text=f'You choose these features {answer_set.values()}and the Rent is \n {rent}')


if __name__ == "__main__":
    app = App()
    app.mainloop()
