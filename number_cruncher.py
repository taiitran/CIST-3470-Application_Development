instruction = "Please enter \"exit\" to quit"
print(f"Instruction: {instruction}\n")

number_list = list()
while True:
    str_number = input("Enter a number: ")

    if str_number.lower() == "exit":
        break

    current_number = float(str_number)
    number_list.append(current_number)

if len(number_list) > 0:
    average = sum(number_list) / len(number_list)

    print("\nCount:", len(number_list))
    print("Sum:", round(sum(number_list), 2))
    print("Average:", round(average, 2))
    print("Max:", max(number_list))
    print("Min:", min(number_list))
else:
    print("\nNo numbers were entered.")

