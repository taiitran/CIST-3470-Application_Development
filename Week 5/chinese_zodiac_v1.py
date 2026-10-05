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