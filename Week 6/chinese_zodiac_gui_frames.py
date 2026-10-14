import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Chinese Zodiac Calculator")
window.geometry("500x300")
window.configure(bg="lightblue")

# Create the title frame
title_frame = tk.Frame(
    window, bg="lightblue"
)
title_frame.pack(pady=20)

# Create and place the label into the title frame.
title_label = tk.Label(
    title_frame,
    text="Chinese Zodiac Calculator",
    font=("Arial", 18, "bold"),
    fg="darkblue",
    bg="lightblue"
)
title_label.pack()

# Create the input frame
input_frame = tk.Frame(
    window,
    bg="lightblue"
)
input_frame.pack(pady=10)

# Create and place widgets into the input frame.
# Birth year
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
    padx=10, pady=10
)

# Email address
email_label = tk.Label(
    input_frame,
    text="Email Address:",
    font=("Arial", 12),
    bg="lightblue"
)
email_label.grid(
    row=1, column=0,
    padx=10, pady=10,
    sticky="e"
)

email_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 12)
)
email_entry.grid(
    row=1, column=1,
    padx=10, pady=10
)

# Create the button frame
button_frame = tk.Frame(
    window, bg="lightblue"
)
button_frame.pack(pady=20)

# Create and place the button into the calculate frame.
calculate_button = tk.Button(
    button_frame,
    text="Find My Zodiac",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="darkblue",
    width=18
)
calculate_button.pack()

window.mainloop()
