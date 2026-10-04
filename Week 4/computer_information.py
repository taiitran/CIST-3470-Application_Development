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