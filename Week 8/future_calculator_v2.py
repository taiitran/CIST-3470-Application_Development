import tkinter as tk
from tkinter import messagebox

# Event handler for Calculate button
def calculate_future_value(event_arg=None):
    try:
        monthly_investment = float(monthly_entry.get())
        yearly_interest_rate = float(interest_entry.get())
        years = int(years_entry.get())

        if monthly_investment <= 0:
            raise ValueError

        if yearly_interest_rate < 0:
            raise ValueError

        if years <= 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a positive monthly investment, "
            "a nonnegative interest rate, and a positive "
            "integer for the number of years.",
            parent=window
        )
        monthly_entry.focus_set()
        return
        

    # Calculate the future value
    monthly_interest_rate = (yearly_interest_rate / 100) / 12
    months = years * 12

    future_value = 0
    principal = 0 

    for i in range(months):
        principal = future_value + monthly_investment
        monthly_interest_amount = principal * monthly_interest_rate
        future_value = principal + monthly_interest_amount

    # Display the result in the Future Value text box
    future_entry.config(state="normal")
    future_entry.delete(0, tk.END)
    future_entry.insert(0, f"${future_value:,.2f}")
    future_entry.config(state="readonly")

    monthly_entry.focus_set()   

# Event handler for Clear button
def clear_fields(event_arg=None):
    monthly_entry.delete(0, tk.END)
    interest_entry.delete(0, tk.END)
    years_entry.delete(0, tk.END)

    future_entry.config(state="normal")
    future_entry.delete(0, tk.END)
    future_entry.config(state="readonly")

    monthly_entry.focus_set()

# Create the main window
window = tk.Tk()
window.title("Future Value Calculator")
window.resizable(False, False)

# create the input frame
input_frame = tk.Frame(window)
input_frame.pack(padx=15, pady=(15, 5))

# create and place Monthly Investment widgets
monthly_label = tk.Label(
    input_frame,
    text="Monthly Investment:",
    font=("Arial", 12)
)
monthly_label.grid(
    row=0, column=0,
    padx=(5, 5), pady=7,
    sticky="w"
)

monthly_entry = tk.Entry(
    input_frame,
    width=23,
    font=("Arial", 12)
)
monthly_entry.grid(
    row=0, column=1,
    padx=5, pady=7
)

# create and place Annual Interest Rate widgets
interest_label = tk.Label(
    input_frame,
    text="Annual Interest Rate (%):",
    font=("Arial", 12)
)
interest_label.grid(
    row=1, column=0,
    padx=(5, 5), pady=7,
    sticky="w"
)

interest_entry = tk.Entry(
    input_frame,
    width=23,
    font=("Arial", 12)
)
interest_entry.grid(
    row=1, column=1,
    padx=5, pady=7
)

# create and place Number of Years widgets
years_label = tk.Label(
    input_frame,
    text="Number of Years:",
    font=("Arial", 12)
)
years_label.grid(
    row=2, column=0,
    padx=(5, 5), pady=7,
    sticky="w"
)

years_entry = tk.Entry(
    input_frame,
    width=23,
    font=("Arial", 12)
)
years_entry.grid(
    row=2, column=1,
    padx=5, pady=7
)

# create and place Future Value widgets
future_label = tk.Label(
    input_frame,
    text="Future Value:",
    font=("Arial", 12)
)
future_label.grid(
    row=3, column=0,
    padx=(5, 5), pady=7,
    sticky="w"
)

future_entry = tk.Entry(
    input_frame,
    width=23,
    font=("Arial", 12),
    state="readonly"
)
future_entry.grid(
    row=3, column=1,
    padx=5, pady=7
)

# keyboard event bindings

monthly_entry.bind("<Return>", calculate_future_value)
monthly_entry.bind("<Escape>", clear_fields)

interest_entry.bind("<Return>", calculate_future_value)
interest_entry.bind("<Escape>", clear_fields)

years_entry.bind("<Return>", calculate_future_value)
years_entry.bind("<Escape>", clear_fields)

# create the button frame
button_frame = tk.Frame(window)
button_frame.pack(pady=(5, 15))

# create the Calculate button
calculate_button = tk.Button(
    button_frame,
    text="Calculate",
    font=("Arial", 12),
    width=14,
    command=calculate_future_value
)
calculate_button.pack(side="left", padx=5)

# create the Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12),
    width=14,
    command=clear_fields
)
clear_button.pack(side="left", padx=5)

# set focus to Monthly Investment
window.after(100, monthly_entry.focus_set)

window.mainloop()