import tkinter as tk
from tkinter import messagebox
from datetime import date

#event handle for Find My Zodiac Button
def show_zodiac(event_arg=None):
    try:
        year = int(year_entry.get())
        current_year = date.today().year

        if year < 1 or year > current_year:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Invalid Birth Year",
            f"Please enter an integer between 1 and {date.today().year}.",
            parent=window
        )
        year_entry.focus_set()
        return

    remainder = year % 12

    match remainder:
        case 0:
            zodiac = "Monkey"
        case 1:
            zodiac = "Rooster"
        case 2:
            zodiac = "Dog"
        case 3:
            zodiac = "Pig"
        case 4:
            zodiac = "Rat"
        case 5:
            zodiac = "Ox"
        case 6:
            zodiac = "Tiger"
        case 7: 
            zodiac = "Rabbit"
        case 8:
            zodiac = "Dragon"
        case 9:
            zodiac = "Snake"
        case 10:
            zodiac = "Horse"
        case 11:
            zodiac = "Goat"

# display the result in a message box
    messagebox.showinfo(
        "Chinese Zodiac Result",
        f"Your Chinese zodiac is {zodiac}!"
    )

    year_entry.focus_set()

# event handler for Clear Button
def clear_fields(event_arg=None):
    year_entry.delete(0, tk.END)

    year_entry.focus_set()

# create the main window
window = tk.Tk()
window.title("Chinese Zodiac Calculator")
window.geometry("500x275")
window.configure(bg="lightblue")

# create the title frame
title_frame = tk.Frame(
    window, bg ="lightblue"
)
title_frame.pack(pady=20)

# create and place the label into the title frame
title_label = tk.Label(
    title_frame,
    text="Chinese Zodiac Calculator",
    font=("Arial", 18, "bold"),
    fg="darkblue",
    bg="lightblue"
)
title_label.pack()

#create the input frame
input_frame = tk.Frame (
    window,
    bg="lightblue"
)
input_frame.pack(pady=10)

# create and place widgets into the input frame.
year_label = tk.Label(
    input_frame,
    text="Birth Year:",
    font=("Arial", 12),
    bg="lightblue"
)
year_label.grid(
    row=0, column=0,
    padx=10, pady=10,
    sticky="e"
)
year_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)
year_entry.grid(
    row=0, column=1,
    padx=10,pady=10,
)
year_entry.bind("<Return>", show_zodiac)
year_entry.bind("<Escape>", clear_fields)

# creat the button frame
button_frame = tk.Frame(
    window, bg ="lightblue"
)
button_frame.pack(pady=20)

# create the Find My Zodiac button
calculate_button = tk.Button(
    button_frame,
    text = "Find My Zodiac",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="darkblue",
    width=14,
    command=show_zodiac
)

#widgets will be packed from left to right within the parent widget.
calculate_button.pack (side="left", padx=5)

# create the clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="gray",
    width=8,
    command=clear_fields
)

# widgets will be packed from left to right within the parent widget.
clear_button.pack(side="left", padx=5)

window.after(100, year_entry.focus_set)
window.mainloop()