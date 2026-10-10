from email.message import EmailMessage

import smtplib

#ask the user to enter the birth year
birth_year = int(input("Enter your birth year: "))

# calculate the remainder
remainder = birth_year % 12

match remainder:
    case 0:
        chinese_zodiac = "Monkey"
    case 1:
        chinese_zodiac = "Rooster"
    case 2:
        chinese_zodiac = "Dog"
    case 3:
        chinese_zodiac = "Pig"
    case 4:
        chinese_zodiac = "Rat"
    case 5:
        chinese_zodiac = "Ox"
    case 6:
        chinese_zodiac = "Tiger"
    case 7:
        chinese_zodiac = "Rabbit"
    case 8:
        chinese_zodiac = "Dragon"
    case 9:
        chinese_zodiac = "Snake"
    case 10:
        chinese_zodiac = "Horse"
    case 11:
        chinese_zodiac = "Sheep"

#display the result
print()
print("Your birth year is:", birth_year)
print("Your Chinese Zodiac sign is:", chinese_zodiac)

# ask the user for an email address
recipient_email = input("Enter your email address: ")
# gmail account used to send the email
sender_email = "your_email@gmail.com"
# use a gmail app password here
app_password = "your_app_password"

# create the email message
message = EmailMessage()
message ["From"] = sender_email
message ["To"] = recipient_email
message ["Subject"] = "Your Chinese Zodiac"

message.set_content(
    "You were born in: " + str(birth_year) + "\n"
    + "Your Chinese Zodiac sign is: " + chinese_zodiac
)

# send the email
try: 
    my_smtp = smtplib.SMTP("smtp.gmail.com", 587)

    my_smtp.starttls()

    my_smtp.login(sender_email, app_password)

    my_smtp.send_message(message)

    my_smtp.quit()

    print("\nThe email was sent.")

except:
    print("\nThe email could not be sent.")



