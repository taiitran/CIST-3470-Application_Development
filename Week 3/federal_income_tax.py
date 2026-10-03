print("Federal Income Tax Calculator")
print()
customer_type = input("Enter filing type (S or Single or M for Married): ")
income = float(input("Enter taxable income: "))

match customer_type:
    case "S" | "s":
        match income:
            case x if x<= 8700:
                tax = x * 0.10
            case x if x <= 35350:
                tax = 870 + (x - 8700) * 0.15
            case x if x <= 85650:
                tax = 4867.50 + (x - 35350) * 0.25
            case x if x <= 178650:
                tax = 17442.50 + (x - 85650) * 0.28
            case x if x <= 388350:
                tax = 43482.50 + (x - 178650) * 0.33
            case x if x > 388350:
                tax = 112683.50 + (x - 388350) * 0.35
    case "M" | "m":
        match income:
            case x if x <= 17400:
                tax = x * 0.10
            case x if x <= 70700:
                tax = 1740 + (x - 17400) * 0.15
            case x if x <= 142700:
                tax = 9735 + (x - 70700) * 0.25
            case x if x <= 217450:
                tax = 27735 + (x - 142700) * 0.28
            case x if x <= 388350:
                tax = 48665 + (x - 217450) * 0.33
            case x if x > 388350:
                tax = 105062 + (x - 388350) * 0.35

print()
print("Filing Status: ", customer_type)
print("Taxable income: ", income)
print("Federal income tax: ", tax)