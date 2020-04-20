import random

hour_challenges = {
    '1' : 'Sit in a tree for an hour and get a timelaps video of it. ',
    '2' : 'Sit on the sidewalk for an hour and get a timelaps video of it. ',
    
}

normal_challenges = {
    '1' : 'Do a hundred crunches',
    '2' : 'Bike to Crystal falls and back',
}

challenge = input('Would you like a challenge (y/n) ')

if challenge.lower() == 'y':
    normal_or_hour = input('Would you like a normal challenge or a hour challenge (normal/hour)? ')
    
    if normal_or_hour.lower() == 'normal':
        num = str(random.randrange(1, len(normal_challenges) + 1))
        print('\nChallenge: ', normal_challenges[num])
    elif normal_or_hour.lower() == 'hour':
        num = str(random.randrange(1, len(hour_challenges) + 1))
        print('\nChallenge: ', hour_challenges[num])
else:
    print('You did not accept a challenge')
