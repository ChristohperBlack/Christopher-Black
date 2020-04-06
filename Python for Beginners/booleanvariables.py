gpa = float(input('What was your Grade Point Average? '))
lg = float(input('What was your lowest grade?'))

if  gpa >= .85 and lg >= .70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made honour roll')