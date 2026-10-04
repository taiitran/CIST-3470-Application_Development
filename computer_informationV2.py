#the "socket" module provides networking-related functions.
# here, we use it to get the computer's host name.
import socket
#the "getpass" module provides functions realted to users and passwords.
import getpass
# we use the "platform" module when we need to get information 
# about the computer's operating system and hardware
import platform
# the "locale" module provides information
# about the computer's regional and language settings.
import locale
# the psutil module provides functions to get information about system resources, such as memory usage.
import psutil

print("My Computer")
print ("=" * 50)

print("\nComputer Information:")
print("-" * 50)
# the gethostname() function (provided by the socket module)
# returns a string, which is the computer's host name.
# what is a host name?
# a host name is the name used to identify the machine on a network
# use ai to know the difference between host name and computer name
print ("Host Name:", socket.gethostname())
# the getuser() function returns a string, which is
# the user name by which the current user logs into the computer.
print("User Name:", getpass.getuser())
# the processor() function returns information about the computer's processor
print("Processor:", platform.processor())

print("\nOperating System Information")
print("-" * 50)
# the system() function returns a string, which is
# the name of the operating system.
# if use macOS, you will see "Darwin". Use AI to know why
print("Operating System:", platform.system())
# the version() function returns a string, which is
# a more detailed version description of the operating system.
print("OS Version:", platform.version())
# the release() function returns a string, which is
# the operating system's release name or number
# e.g., if you see "11", it means you are using Windows 11.
print("OS Release:", platform.release())
# the machine() function returns a string, which is
# the computer's machine architecture.
# e.g., if you see "AMD64", it means you are using a 64-bit x86 -compatible computer.
print("System Type:", platform.machine())
# the getlocale() functions returns a tuple.
# getlocale()[0] gets the first item in this tuple
print("System Language:", locale.getlocale()[0])

print("\nMemory Information:")
print("-" * 50)
# the following function returns/creates an dobject which stores different memory-related data
memory = psutil.virtual_memory()
# memory.total gives the total amount of RAM in bytes.
print("Total Memory:", round(memory.total / (1024 ** 3), 2), "GB")
# memory.available gives the amount of RAM that is available to use.
print("Available Memory:", round(memory.available / (1024 ** 3), 2), "GB")
# memory.used gives the amount of RAM being used.
print("Used Memory:", round(memory.used / (1024 ** 3), 2), "GB")
# memory.percent gibes ther percentage of physical memory currently in use.
print("Memory Usage:", memory.percent, "%")
# the variablles total, available, used and percent are known as the attributes of the object
# memory_dict = memory._asdict()
# print (memory_dict)

print("\nWindows C: Drive Information")
print("-" * 50)
# the following function returns/creates an object which stores different disk-related data
disk = psutil.disk_usage("C:\\")
# the following attribute gives the total size of the C: drive space in bytes.
print("Total Disk Space:", round(disk.total / (1024 ** 3), 2), "GB")
# the following attribute gives how much disk space is still available.
print("Free Disk Space:", round(disk.free / (1024 ** 3), 2), "GB")
# the following attribute gives how much disk space is being used.
print("Used Disk Space:", round(disk.used / (1024 ** 3), 2), "GB")
print("Disk Usage:", disk.percent, "%")
