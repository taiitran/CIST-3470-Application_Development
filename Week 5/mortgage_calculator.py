from email.message import EmailMessage
import smtplib

def main():
    print("Program: Mortgage Calculator")
    print("Developer: Tai Tran")
    print("Date: October 10, 2026")
    print()

    try:
        loan_amount = float(input("Enter mortage loan amount: "))
        annual_interest_rate = float(input("Enter annual interest rate: "))
        loan_term_years = int(input("Enter loan term in years: "))
        recipient_email = input("Enter your email address: ")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    p = loan_amount
    n = loan_term_years * 12

    if annual_interest_rate == 0:
        monthly_payment = p / n
    else:
        r = annual_interest_rate / 100 / 12
        monthly_payment = (p * r) / (1 - (1 + r) ** -n)

    print("Your monthly mortgage payment is", round(monthly_payment, 2))

    sender_email = "your_email@gmail.com"
    app_password = "your_app_password"

    message = EmailMessage()
    message ["From"] = sender_email
    message ["To"] = recipient_email
    message ["Subject"] = "Your Mortgage Payment Results"

    message.set_content(
        "Your loan amount is: " + str(loan_amount) + "\n"
        + "Annual interest rate: " + str(annual_interest_rate) + "\n"
        + "Loan term in years: " + str(loan_term_years) + "\n"
        + "Your monthly mortgage payment is: " + str(round(monthly_payment, 2))
    )

    try: 
        my_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        my_smtp.starttls()
        my_smtp.login(sender_email, app_password)
        my_smtp.send_message(message)
        my_smtp.quit()
        print("\nMortage payment results emailed successfully.")
    except:
        print("\nThe email could not be sent.")

if __name__ == "__main__":
    main()