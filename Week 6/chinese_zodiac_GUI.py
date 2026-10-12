import tkinter as tk

window = tk.Tk()
window.title("Chinese Zodiac Calculator")
window.geometry("500x300")

year_label = tk.Label(
    window,
    text="Enter your birth year:"
)
year_label.pack(pady=10)

year_entry = tk.Entry(window)
year_entry.pack(pady=10)

calculate_button = tk.Button(
    window,
    text="Find My Zodiac"
)
calculate_button.pack(pady=10)

window.mainloop()
