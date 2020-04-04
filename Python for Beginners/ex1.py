fn = input ('Tell me your full name ')
age = int(input ('How old will you be at the end of the year '))
mom = int (input('How old will your mom be at the end of the year '))

year = (2020 - age) + 100
number = (2020 - age) + 1000
mom_age = (mom - age)

print(f'\nHello {fn}! Your mom was {mom_age} when you where born and did your know that in the year {year} you will be 100 and in the year {number} you will be 1000\n')

if age >= 50:
    print("Yay, you're old")
else:
    print("Yay, you're young")