import math

# Sum List

listA = [1,5,6,7,4,6,4]
varA = sum(listA)

print(varA)

print('\n' + '*'*8 + '\n')

# Count number of times "Olympic" is used

strA = 'I love Olympic ! But doo I mean the Olympic mountains or Olympic college?'
print(strA)

listA = strA.split()
varA = strA.count('Olympic')

print('The word Olympic appears ' + str(varA) + ' times within this string.')

# Print only words 3 characters or longer

varA = ' '

for i in range(len(listA)):
    if len(listA[i]) > 3:
        varA = varA + listA[i] + ' '

listA = varA.split()
print('\nWords larger than 3 characters;\n' + str(listA))

print('\n' + '*'*8 + '\n')

# Count negative and positive numbers in a list.

listB = [-10,1,90,-4,-7,9,70]
posVars = 0
negVars = 0

for i in range(len(listB)):
    if listB[i] >= 0:
        posVars += 1
    else:
        negVars += 1

print(listB)
print('Positive Values: ' + str(posVars) + ' Negative Values: ' + str(negVars))

print('\n' + '*'*8 + '\n')

# Square every number and post the new list

listB = [4,9,90,20,7,121,70]
print('Old list: ' + str(listB))

for i in range(len(listB)):
    listB[i] = math.sqrt(listB[i])
    
print('New list: ' + str(listB))
