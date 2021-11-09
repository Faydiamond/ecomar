# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:15:03 2021

@author: FabiDiamanti
"""
#instalar la libreria tkcalendar

import tkinter as tk
import _tkinter
import  tkcalendar as  tc
from datetime import datetime


ventana = tk.Tk()
ventana.geometry('700x400')
ventana.title('Hotel ECOMAR')
price = tk.IntVar()

price_lbl = tk.Label (ventana, text = 'Ingrese el precio por dia ')
price_lbl.place(x=20 , y = 10)
price_box = tk.Entry(ventana, textvariable = price)
price_box.place(x= 160, y= 10)

#CALENDARIO #1
calendar = tc.Calendar(ventana, selectmode='day', year = 2021 , month=11 )
calendar.place(x = 20,y=50)
#CALENDARIO #2
calendar2 = tc.Calendar(ventana, selectmode='day', year = 2021 , month=11)
calendar2.place(x = 350,y=50)

def calculate():
    if (price_box.get() == ''):
        error.config(text='Error, por favor ingrese un numero')
        #print('Error, por favor ingrese un numero')
    else:
        try :
            price_float= float(price.get())
            date1 = calendar.get_date();
            date2 = calendar2.get_date();
            if(date1 == ''  or date2 == '' ):
                #print ('por favor seleccione una fecha para cada calendario')
                error.config(text='Error,por favor seleccione una fecha para cada calendario ')
            else :
                #calcular diferencia de dias
                date1 = datetime.strptime(date1, '%m/%d/%y')
                date2 = datetime.strptime(date2, '%m/%d/%y')
                dif_days = (date2 - date1) .days
                
                #print (' resultado  dias::  ',  dif_days.days , ' caja ',price_box.get() )
                total = 0
                off   = 0
                sub_total = 0
                if(dif_days > 6  and dif_days  <= 11 ):
                    sub_total = (price_float * dif_days)
                    off   = (sub_total*0.15)
                    total = sub_total - off
                elif (dif_days > 11 and dif_days  <= 16 ):
                    sub_total = (price_float * dif_days)
                    off   = (sub_total*0.16)
                    total = sub_total - off
                elif (dif_days >= 16):
                    sub_total = (price_float * dif_days)
                    off   = (sub_total*0.20)
                    total = sub_total - off
                    
                result_sub_total.config(text=sub_total)
                result_off_label.config(text=off)
                result_total.config(text=total)
                
           
        except :
            #print (' No es un Numero ')
            #result.config(text='Error, por favor ingrese un numero')
             error.config(text='Error, No es un Numero ')


calculate_btn = tk.Button(ventana ,text='Calcular Precio', command = calculate)
calculate_btn.place(x = 270, y= 250)

sub_total_label = tk.Label (ventana,text = 'Sub Total :' )
sub_total_label.place(x = 200, y= 305)

result_sub_total = tk.Label (ventana,text = '' )
result_sub_total.place(x = 270, y= 305)

off_label = tk.Label (ventana,text = ' Descuento :' )
off_label.place(x = 200, y= 325)

result_off_label = tk.Label (ventana,text = '' )
result_off_label.place(x = 270, y= 325)

total_label = tk.Label (ventana,text = ' total :' )
total_label.place(x = 200, y= 345)

result_total = tk.Label (ventana,text = '' )
result_total.place(x = 270, y= 345)

error  = tk.Label (ventana,text = '', fg='#ED2727' )
error .place(x = 270, y= 360)

ventana.mainloop()