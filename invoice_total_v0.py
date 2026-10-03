#Ask the user for the customer type
customer_type = input("Enter customer type: ")
# Ask the user for the invoice subtotal
subtotal = float(input("Enter invoice subtotal: "))

# determine the discount percentage
match customer_type:
    case "R" | "r":
        match subtotal:
            case x if x < 100:
                discount_percent = 0
            case x if x >=100 and x < 250:
                discount_percent = 0.1
            case x if x < 500:
                discount_percent = 0.25
            case _:
                discount_percent = 0.3
    case "C" | "c":
        discount_percent = 0.2
    case "T" | "t":
        match subtotal:
            case x if x < 500:
                discount_precent = 0.4
            case _:
                discount_percent = 0.5
    case _:
        discount_percent = 0.1

# display the result
print()
print ("Customer type:", customer_type)
print ("Invoice subtotal:", subtotal)
print ("Discount percent:", discount_percent)


        
        
