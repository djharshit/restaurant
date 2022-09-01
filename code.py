'''
Restuarant Managment System - By Harshit M

'''

# Importing all the libraries
import tkinter as tk
import random

from datetime import datetime
from PIL import Image, ImageTk

# Defing the window and its properties
wind = tk.Tk()
wind.geometry('1200x650')
wind.title('Restaurant Management system')

head_frame = tk.Frame(wind, bd=10, relief=tk.GROOVE)
head_frame.pack(side=tk.TOP)

item_frame = tk.Frame(wind, bd=5, height=400, width=300, relief=tk.RAISED)
item_frame.pack(side=tk.LEFT ,fill='both', expand=1)

bill_frame = tk.Frame(wind, bd=5, height=400, width=300, relief=tk.RAISED)

image = Image.open('logo.png')
logo_image = ImageTk.PhotoImage(image.resize((300, 120)))

head_label = tk.Label(head_frame, font=('aria', 30, 'bold'), text='Restaurant Billing System',
                      image=logo_image, fg='white', bg='brown', width=1150,
                      compound=tk.LEFT)
head_label.grid(row=0, column=0)

localtime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# ======== Tk Variables ========
idli_var = tk.StringVar()
dosa_var = tk.StringVar()
pongal_var = tk.StringVar()
vadai_var = tk.StringVar()
poori_var = tk.StringVar()
tea_var = tk.StringVar()
coffee_var = tk.StringVar()

bill_no_var = tk.StringVar()
date_var = tk.StringVar()
user_cost_var = tk.StringVar()
tax_var = tk.StringVar()
total_cost_var = tk.StringVar()

# ======== Menu Items ========

idli_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Idli Rs.30',
                      width=12, fg='blue4', bd=10, anchor='w')
idli_label.grid(row=1, column=0)
idli_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=idli_var,
                      bd=6, width=8, bg='misty rose', justify='right')
idli_entry.grid(row=1, column=1)

dosa_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Dosa Rs.45',
                      width=12, fg='blue4', bd=10, anchor='w')
dosa_label.grid(row=2, column=0)
dosa_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=dosa_var,
                      bd=6, width=8, bg='misty rose', justify='right')
dosa_entry.grid(row=2, column=1)

pongal_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Pongal Rs.55',
                        width=12, fg='blue4', bd=10, anchor='w')
pongal_label.grid(row=3, column=0)
pongal_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=pongal_var,
                        bd=6, width=8, bg='misty rose', justify='right')
pongal_entry.grid(row=3, column=1)

vadai_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Vadai Rs.20',
                       width=12, fg='blue4', bd=10, anchor='w')
vadai_label.grid(row=4, column=0)
vadai_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=vadai_var,
                       bd=6, width=8, bg='misty rose', justify='right')
vadai_entry.grid(row=4, column=1)

poori_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Poori Rs.50',
                       width=12, fg='blue4', bd=10, anchor='w')
poori_label.grid(row=5, column=0)
poori_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=poori_var,
                       bd=6, width=8, bg='misty rose', justify='right')
poori_entry.grid(row=5, column=1)

tea_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Tea Rs.15',
                     width=12, fg='blue4', bd=10, anchor='w')
tea_label.grid(row=6, column=0)
tea_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=tea_var,
                     bd=6, width=8, bg='misty rose', justify='right')
tea_entry.grid(row=6, column=1)

coffee_label = tk.Label(item_frame, font=('aria', 20, 'bold'), text='Coffee Rs.20',
                        width=12, fg='blue4', bd=10, anchor='w')
coffee_label.grid(row=7, column=0)
coffee_entry = tk.Entry(item_frame, font=('ariel', 20, 'bold'), textvariable=coffee_var,
                        bd=6, width=8, bg='misty rose', justify='right')
coffee_entry.grid(row=7, column=1)


def generate_bill():
    '''
    Genrete the bill and display in the bill frame
    '''
    bill_no = str(random.randint(15000, 50000))
    bill_no_var.set(bill_no)
    date_var.set(localtime)

    try:
        qd = int(dosa_var.get())
    except:
        qd = 0
    try:
        qp = int(pongal_var.get())
    except:
        qp = 0
    try:
        qv = int(vadai_var.get())
    except:
        qv = 0
    try:
        qpoori = int(poori_var.get())
    except:
        qpoori = 0
    try:
        qcof = int(coffee_var.get())
    except:
        qcof = 0
    try:
        qi = int(idli_var.get())
    except:
        qi = 0
    try:
        qt = int(tea_var.get())
    except:
        qt = 0

    costofdosa = qd * 45
    costofpongal = qp * 55
    costofvadai = qv * 20
    costofpoori = qpoori * 50
    costofcoffee = qcof * 20
    costofidli = qi * 30
    costoftea = qt * 15

    bill_frame.pack(side=tk.RIGHT, fill='both', expand=1)
    bill_frame.configure(background='light yellow')

    bill_label = tk.Label(bill_frame, font=('aria', 18, 'bold'), text='Bill No.',
                          bg='light yellow', width=12, bd=20, anchor='w')
    bill_label.grid(row=1, column=0)
    bill_entry = tk.Entry(bill_frame, font=('ariel', 18, 'bold'), textvariable=bill_no_var,
                          bd=6, width=17, bg='brown', fg='white',justify='right')
    bill_entry.grid(row=1, column=1)

    date_label = tk.Label(bill_frame, font=('aria', 18, 'bold'), text='Date',
                        bg='light yellow', width=12, bd=10, anchor='w')
    date_label.grid(row=2, column=0)
    date_entry = tk.Entry(bill_frame, font=('ariel', 18, 'bold'), textvariable=date_var,
                        bd=6, width=17, bg='Pale Green1', justify='right')
    date_entry.grid(row=2, column=1)

    cost_label = tk.Label(bill_frame, font=('aria', 18, 'bold'), text='Cost',
                          bg='light yellow',width=12, bd=10, anchor='w')
    cost_label.grid(row=3, column=0)
    cost_entry = tk.Entry(bill_frame, font=('ariel', 18, 'bold'), textvariable=user_cost_var,
                          bd=6, width=17, bg='Pale Green1', justify='right')
    cost_entry.grid(row=3, column=1)

    tax_label = tk.Label(bill_frame, font=('aria', 18, 'bold'), text='Tax',
                         bg='light yellow', width=12, bd=10, anchor='w')
    tax_label.grid(row=5, column=0)
    tax_entry = tk.Entry(bill_frame, font=('ariel', 18, 'bold'), textvariable=tax_var,
                         bd=6, width=17, bg='Pale Green1', justify='right')
    tax_entry.grid(row=5, column=1)

    total_label = tk.Label(bill_frame, font=('aria', 18, 'bold'), text='Total',
                           bg='light yellow', width=12, bd=10, anchor='w')
    total_label.grid(row=6, column=0)
    total_entry = tk.Entry(bill_frame, font=('ariel', 18, 'bold'), textvariable=total_cost_var,
                           bd=6, width=17, bg='brown', fg='white', justify='right')
    total_entry.grid(row=6, column=1)

    costofmeal = costofdosa + costoftea + costofpongal + costofvadai + costofpoori + costofcoffee + costofidli

    costofmeal_disp = f'Rs. {costofmeal:.2f}'
    paytax = costofmeal * 0.18
    paytax_disp = f'Rs. {paytax:.2f}'
    totalcost = paytax + costofmeal
    totalcost_disp = f'Rs. {totalcost:.2f}'

    user_cost_var.set(costofmeal_disp)
    tax_var.set(paytax_disp)
    total_cost_var.set(totalcost_disp)


def reset():
    '''
    Reset the bill to 0 values when user press `reset button`
    '''
    dosa_var.set('')
    pongal_var.set('')
    vadai_var.set('')
    poori_var.set('')
    idli_var.set('')
    tea_var.set('')
    coffee_var.set('')

    date_var.set('')

    bill_frame.pack_forget()


total_button = tk.Button(item_frame, bd=5, fg='black', font=('ariel', 16, 'bold'),
                         width=14, text='CALCULATE BILL', bg='SteelBlue1',
                         command=generate_bill)
total_button.grid(row=9, column=0, padx=10, pady=10)

reset_button = tk.Button(item_frame, bd=5, fg='black', font=('ariel', 16, 'bold'),
                         width=10, text='RESET', bg='SteelBlue1',
                         command=reset)
reset_button.grid(row=9, column=1, padx=10, pady=10)

exit_button = tk.Button(item_frame, bd=5, fg='black', font=('ariel', 16, 'bold'),
                        width=10, text='EXIT', bg='SteelBlue1',
                        command=wind.destroy)
exit_button.grid(row=9, column=2, padx=10, pady=10)

wind.mainloop()
