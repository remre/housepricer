
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

from datetime import datetime
import tkinter as tk
from tkinter import EXTENDED, MULTIPLE, SINGLE,  ttk, Label, Entry, Listbox, Scrollbar
from tkinter.messagebox import YES
from tkinter.tix import COLUMN
from tokenize import Single
from turtle import width
from linearregressionhouse import df2, Scaler, one_hot_encode, convertto_int, model,df3
import pandas as pd


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.root = Tk()
        self.title('House Price Prediction Tool')
        self.geometry("800x400")

        self.name_var = tk.StringVar()
        # self.floor_number = Listbox(self,width=5,height=5,selectmode=SINGLE,exportselection=0)
        self.floor_number = ttk.Combobox(self,width=5)
        self.bedroom_number = ttk.Combobox(self,width=5)
        self.areatypes = ttk.Combobox(self,width=15)
        self.city = ttk.Combobox(self,width=10)
        self.point_o_contact = ttk.Combobox(self,width=10)
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
        titlebed = Label(self,text="Bedrooms")
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
        area_types  =  list(sorted(df2['Area Type'].unique()))
        self.areatypes['values'] = area_types


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
        bathroomtitle = Label(self,text='Bathroom')
        # bathroom = Listbox(self, width=5,height=5,selectmode=SINGLE,exportselection=0)
        bathroom_number  = list(sorted(df2['Bathroom'].unique()))
        self.bathroom['values'] = bathroom_number
        
        # for i in range(len(bathroom_number)):
        #     bathroom.insert(i,f'{bathroom_number[i]}')
        
        bathroomtitle.grid(column=8,row=0,**padding)
        self.bathroom.grid(column=8,row=1,**padding)
        self.bathroom.current(0)


        # Point of Contact
        pointocontacttitle = Label(self,text='Point of Contact')
        point_o_contact  =  list(sorted(df2['Point of Contact'].unique()))
        self.point_o_contact['values'] = point_o_contact


        pointocontacttitle.grid(column=9,row=0,**padding)
        self.point_o_contact.grid(column=9,row=1,**padding)
        self.point_o_contact.current()






        
        # Button
        # self.graph = Listbox(self,width=10,selectmode=SINGLE)
        # for col in range(len(df2.columns)):

        #     self.graph.insert(col,f'{df2.columns[col]}')
        
        # graphtitle = Label(text='Choose the feature you want to see in graph')
        # graphtitle.grid(column=9,row=0)
        # self.graph.grid(column=9,row=1)
        # def selected_item():
        #     for i in self.graph.curselection():
        #         # submit_button.config(command=buttonact(self.graph.get(i)))
        #         a = ttk.Label(text=f'this is the text {self.graph.get(i)}')
        #         a.grid(column=11,row=1)
        #         return  self.graph.get(i)
        # x_value = selected_item()
            #    self.graph.get(i)
        # print(selected_item())
        # submit_button = ttk.Button(self, text='Graph',command=selected_item)
        # submit_button.grid(column=10, row=1, **padding)
        # Output label
        rent = 500
        self.output_label = ttk.Label(self,text='Select features above and see the predicted rent that you gonna pay!!')
        self.output_label.grid(column=0, row=10, columnspan=15,rowspan=5, **padding)
        submit_button = ttk.Button(self, text='Submit',command=self.submit)
        submit_button.grid(column=11, row=1, **padding)



    def submit(self):
        # for i in self.floor_number.curselection():
        answer_set = {
                        'floor level': [self.floor_number.get()],
                        'BHK': [self.bedroom_number.get()],
                        'Area Type': [self.areatypes.get()],
                        'City': [self.city.get()],
                        'Furnishing Status': [self.furnishes.get()],
                        'Tenant Preferred': [self.preftenat.get()],
                        'Bathroom':[self.bathroom.get()],
                        'Point of Contact' : [self.point_o_contact.get()],
                        'Size' :[round(df2.loc[df2['Bathroom']==round(df2['Bathroom'].mean())]['Size'].mean())],
                        'total floor' : [round(df2['total floor'].mean())],
                        'year' : [datetime.now().year],
                        'month':[datetime.now().month]
        }
        dff = pd.DataFrame.from_dict(answer_set)
        tonum_cols = [ 'BHK','floor level','year','month','Bathroom']
        
        convertto_int(dff,tonum_cols)
        # print(dff.info())
        columnss = list(dff.select_dtypes(include='object').columns)
        for nom in columnss:

            dff = one_hot_encode(dff,nom)

        Scaler(dff)
        
        lack_list = list(df3.columns.difference(dff.columns))
        lack_list.remove('Rent')
        for i in lack_list:
            dff[i] = 0
        print(dff.head())
        print(f'df3 columns \n{df3.columns}')

        # print(dff.columns.difference(df2.columns))
        result = model.predict(dff)
        # print(result)

        # for i in answer_set


        self.output_label.config(text=f'You choose these features {list(answer_set.values())} and the Rent is \n {result}')
        # print(df2.columns)
        # df2.loc[0,['Floor','NAME']] = [100,'Python']
if __name__ == "__main__":
    app = App()
    app.mainloop()
