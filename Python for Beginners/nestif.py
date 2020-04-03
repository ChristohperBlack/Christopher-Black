country = input('What country do you live in?')
country = country.capitalize()

tax = 0.0

if country == 'Canada':
    province = input('What province do you live in? ' )
    province = province.capitalize()

    if province in('Alberta','Nunavut','Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0

print (tax)

