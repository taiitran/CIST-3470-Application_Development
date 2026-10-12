import tkinter as tk

window = tk.Tk()
window.title("Chinese Zodiac Calculator")
window.geometry("400x200")

year_label = tk.Label(
    window,
    text="Birth Year:"
)

year_label.grid(
    row=0, column=0,
    padx=10, pady=10,
    sticky="e"
)

year_entry = tk.Entry(window)
year_entry.grid(
    row=0, column=1,
    padx=10, pady=10
)

email_label = tk.Label(
    window,
    text="Email Address:"
)
email_label.grid(
    row=1, column=0,
    padx=10, pady=10,
    sticky="e"
)

email_entry = tk.Entry(window)
email_entry.grid(
    row=1, column=1,
    padx=10, pady=10
)

calculate_button = tk.Button(
    window,
    text="Find My Zodiac"
)
calculate_button.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=15
)

window.mainloop()
