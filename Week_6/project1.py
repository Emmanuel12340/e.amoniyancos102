import tkinter as tk
from tkinter import messagebox

def calculate_fee():
    location = location_var.get()
    weight = weight_entry.get()
    try: 
        weight = float(weight_entry.get())
    except ValueError:
        messagebox.showerror("invalid input", "please enter a valid value for the weight")
        return
    if location == "Ibeju-Lekki":
        if weight >= 10:
            fee = 5000
        else:
            fee = 3500
    elif location == "Epe":
        if weight >= 10:
            fee = 10000
        else:
            fee = 5000
    else:
        messagebox.showerror("invalid Location", "please enter a valid location")
        return
    result_label.config(text=f"Delivery Fee: N{fee}")

window = tk.Tk()
window.title("Delivery Fee Calculator")

tk.Label(window, text="select Location:").pack()
location_var = tk.StringVar()
location_menu = tk.StringVar()
location_menu = tk.OptionMenu(window,location_var, "Ibeju-Lekki","Epe")
location_menu.pack()

tk.Label(window, text= "Enter weight (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Button(window, text="Calculate Fee", command=calculate_fee).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()