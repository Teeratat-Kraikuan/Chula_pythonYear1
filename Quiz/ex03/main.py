zodiac_years = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]

month, year = [int(i) for i in input().split()]
if month == 1:
    print(zodiac_years[year % 12 - 1])
else:
    print(zodiac_years[year % 12])