import tkinter as tk 
import socket
import getpass
import platform
import locale
import psutil
import os

from tkinter import messagebox

messagebox.showinfo(
    "Author: Tai Tran",
    "Welcome to my Computer!"
)

# gets the computer information about the memory and drive space
memory = psutil.virtual_memory()

# gets the computer information about the disk space
disk = psutil.disk_usage('/')

# create the main window
window = tk.Tk()
window.title("My Computer")
window.geometry("600x700")

# create the computer information frame
computer_frame = tk.LabelFrame(window, text="Computer Information")
computer_frame.pack(fill="x", padx=15, pady=10)

host_label = tk.Label(computer_frame, text="Host Name:")
host_label.grid(row=0, column=0, padx=10, pady=8, sticky="e")
host_info = tk.Label(computer_frame, text=socket.gethostname())
host_info.grid(row=0, column=1, padx=10, pady=8, sticky="w")

user_label = tk.Label(computer_frame, text="User Name:")
user_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")
user_info = tk.Label(computer_frame, text=getpass.getuser())
user_info.grid(row=1, column=1, padx=10, pady=8, sticky="w")

processor_label = tk.Label(computer_frame, text="Processor:")
processor_label.grid(row=2, column=0, padx=10, pady=8, sticky="e")
processor_info = tk.Label(computer_frame, text=platform.processor() or platform.machine(), wraplength=420, justify="left")
processor_info.grid(row=2, column=1, padx=10, pady=8, sticky="w")

# create the operation system information frame
os_frame = tk.LabelFrame(window, text="OS Information")
os_frame.pack(fill="x", padx=15, pady=10)

os_label = tk.Label(os_frame, text="Operating System:")
os_label.grid(row=0, column=0, padx=10, pady=6, sticky="e")
os_info = tk.Label(os_frame, text=platform.system())
os_info.grid(row=0, column=1, padx=10, pady=6, sticky="w")

version_label = tk.Label(os_frame, text="OS Version:")
version_label.grid(row=1, column=0, padx=10, pady=6, sticky="e")
version_info = tk.Label(os_frame, text=platform.version(), wraplength=400, justify="left")
version_info.grid(row=1, column=1, padx=10, pady=6, sticky="w")

release_label = tk.Label(os_frame, text="OS Release:")
release_label.grid(row=2, column=0, padx=10, pady=6, sticky="e")
release_info = tk.Label(os_frame, text=platform.release())
release_info.grid(row=2, column=1, padx=10, pady=6, sticky="w")

type_label = tk.Label(os_frame, text="System Type:")
type_label.grid(row=3, column=0, padx=10, pady=6, sticky="e")
type_info = tk.Label(os_frame, text=platform.machine())
type_info.grid(row=3, column=1, padx=10, pady=6, sticky="w")

language_label = tk.Label(os_frame, text="System Language:")
language_label.grid(row=4, column=0, padx=10, pady=6, sticky="e")
language_info = tk.Label(os_frame, text=locale.getlocale()[0] or "Unknown")
language_info.grid(row=4, column=1, padx=10, pady=6, sticky="w")

# creates the memory information frame
memory_frame = tk.LabelFrame(window, text="Memory Information")
memory_frame.pack(fill="x", padx=15, pady=10)

total_memory_label = tk.Label(memory_frame, text="Total Memory:")
total_memory_label.grid(row=0, column=0, padx=10, pady=6, sticky="e")
total_memory_info = tk.Label(memory_frame, text=str(round(memory.total / (1024 ** 3), 2)) + " GB")
total_memory_info.grid(row=0, column=1, padx=10, pady=6, sticky="w")

available_memory_label = tk.Label(memory_frame, text="Available Memory:")
available_memory_label.grid(row=1, column=0, padx=10, pady=6, sticky="e")
available_memory_info = tk.Label(memory_frame, text=str(round(memory.available / (1024 ** 3), 2)) + " GB")
available_memory_info.grid(row=1, column=1, padx=10, pady=6, sticky="w")

used_memory_label = tk.Label(memory_frame, text="Used Memory:")
used_memory_label.grid(row=2, column=0, padx=10, pady=6, sticky="e")
used_memory_info = tk.Label(memory_frame, text=str(round(memory.used / (1024 ** 3), 2)) + " GB")
used_memory_info.grid(row=2, column=1, padx=10, pady=6, sticky="w")

memory_usage_label = tk.Label(memory_frame, text="Memory Usage:")
memory_usage_label.grid(row=3, column=0, padx=10, pady=6, sticky="e")
memory_usage_info = tk.Label(memory_frame, text=str(memory.percent) + "%")
memory_usage_info.grid(row=3, column=1, padx=10, pady=6, sticky="w")

# creates the drive information frame
drive_frame = tk.LabelFrame(window, text="Windows C: Drive Information")
drive_frame.pack(fill="x", padx=15, pady=10)

total_disk_label = tk.Label(drive_frame, text="Total Disk Space:")
total_disk_label.grid(row=0, column=0, padx=10, pady=6, sticky="e")
total_disk_info = tk.Label(drive_frame, text=str(round(disk.total / (1024 ** 3), 2)) + " GB")
total_disk_info.grid(row=0, column=1, padx=10, pady=6, sticky="w")

free_disk_label = tk.Label(drive_frame, text="Free Disk Space:")
free_disk_label.grid(row=1, column=0, padx=10, pady=6, sticky="e")
free_disk_info = tk.Label(drive_frame, text=str(round(disk.free / (1024 ** 3), 2)) + " GB")
free_disk_info.grid(row=1, column=1, padx=10, pady=6, sticky="w")

used_disk_label = tk.Label(drive_frame, text="Used Disk Space:")
used_disk_label.grid(row=2, column=0, padx=10, pady=6, sticky="e")
used_disk_info = tk.Label(drive_frame, text=str(round(disk.used / (1024 ** 3), 2)) + " GB")
used_disk_info.grid(row=2, column=1, padx=10, pady=6, sticky="w")

disk_usage_label = tk.Label(drive_frame, text="Disk Usage:")
disk_usage_label.grid(row=3, column=0, padx=10, pady=6, sticky="e")
disk_usage_info = tk.Label(drive_frame, text=str(disk.percent) + "%")
disk_usage_info.grid(row=3, column=1, padx=10, pady=6, sticky="w")
 

window.mainloop()
