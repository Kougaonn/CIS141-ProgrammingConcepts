'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''

def count_vowels(strA):
    varA = strA.count('a') + strA.count('i') + strA.count('u') + strA.count('e') + strA.count('u')
    print(varA)

# count_vowels('I like men')

'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''

def is_palindrome(s):
    match = True
    strA = s.lower()
    for i in range(len(strA)):
        if strA[i] != strA[len(strA)-i-1]:
            match = False
    print(match)

'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''

def type_advantage(attacker,defender):
    if attacker == 'Fire':
        if defender == 'Grass':
            print('Super Effective!')
        if defender == 'Fire':
            print('Neutral')
        if defender == 'Water':
            print('Not Very Effective...')
    elif attacker == 'Grass':
        if defender == 'Grass':
            print('Neutral')
        if defender == 'Fire':
            print('Not Very Effective...')
        if defender == 'Water':
            print('Super Effective!')
    elif attacker == 'Water':
        if defender == 'Grass':
            print('Not Very Effective...')
        if defender == 'Fire':
            print('Super Effective!')
        if defender == 'Water':
            print('Neutral')

# type_advantage('Water','Water')

'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''

def ferry_fare(age, vehicle):
    if vehicle == True:
        if age >= 65:
            print('$15')
        elif age >= 18:
            print('$20')
        else:
           print('Free')
    else:
        if age >= 65:
            print('$5')
        elif age >= 18:
            print('$10')
        else:
           print('Free')

# ferry_fare(4,True)

'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
'''

def level_up(exp):
    if exp >= 200:
        print('Level 3')
    elif exp >= 100:
        print('Level 2')
    else:
        print('Level 1')

# level_up(800)
