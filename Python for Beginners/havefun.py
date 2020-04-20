import random
fn = input('Tell me your full name ')
age = int(input('How old will you be at the end of the year '))
mom = int (input('How old will your mom be at the end of the year '))

challenge = input('Would you like a challenge (y/n) ') 

challenges = {
    '1' : 'Challenge: Sit in a tree for an hour and get a timelaps video of it.',
    '2' : 'Challenge: Sit on the sidewalk for an hour and get a timelaps video of it.',
    
}

if challenge.lower() == 'y':
    num = str(random.randrange(1, len(challenges) + 1))
    print('\n'challenges[num])
else:
    print('You did not accept a challenge')


year = (2020 - age) + 100
number = (2020 - age) + 1000
mom_age = (mom - age)

print(f'\nHello {fn}!\n Your mom was {mom_age} when you where born,\n and did your know that in the year {year} you will be 100 and in the year {number} you will be 1000\n')

if age >= 50:
    print("Yay, you're old\n")
else:
    print("Yay, you're young\n")