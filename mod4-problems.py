# Boolean Truth Table 

# if A or not B:
#   True True = True
#   False True = False
#   True False = True
#   False False = True

# Headlights

varA = int(input('How dark is it outside? '))

if varA >= 8 :
    print('Headlight = ON')
else :
    print('Headlight = OFF')

print('\n' + '-' * 8 + '\n')

# Bank Balance

varA = int(input('What is your bank balance? '))

if varA >= 100 :
    print('Congratulations! Your balance is in good standing!')
else :
    print('I\'m sorry, it appears your balance is not in good standing.\n We will be proceeding with closing your account.')

print('\n' + '-' * 8 + '\n')

# Movie Theater Age-Checking

varA = int(input('How old are you? '))

if varA >= 18:
    print('Here are the movies you may attend:\n R = Yes\n PG-13 = Yes\n G = Yes')
elif  varA >= 13:
    print('Here are the movies you may attend:\n R = No\n PG-13 = Yes\n G = Yes')
else :
    print('Here are the movies you may attend:\n R = No\n PG-13 = No\n G = Yes')
    
print('\n' + '-' * 8 + '\n')

# Shipping Costs

varA = int(input('Thank you for shopping with us today.\n What is your total? '))

if varA < 50:
    varA = varA + 5
    print('Your total will be $' + str(varA))
else:
    print('Your total will be $' + str(varA))
    
print('\n' + '-' * 8 + '\n')
