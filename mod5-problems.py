# While Counting; Sum

varA = int(input('Give an integer. '))
varB = 1
varResult = 0

while varB < varA + 1:
    varResult = varResult + varB
    varB += 1
   
print(varResult)
print('\n', '-'*8,'\n')


# Print Every Character
strA = "Olympic College"

for i in range(0,len(strA),1):
    print(strA[i])

print('\n', '-'*8,'\n')
print('End Of Loop.')
print('\n', '-'*8,'\n')

# Print every other character

for i in range(2,21,2):
    print(i)

print('\n', '-'*8,'\n')
print('End Of Loop.')
print('\n', '-'*8,'\n')

#Nested multiplication table

for i in range(1,6,1):
    strA = ' '
    for o in range(1,6):
        strA = strA + ' ' + str(o*i)
    print(strA)

print('\n', '-'*8,'\n')
print('End Of Loop.')
print('\n', '-'*8,'\n')

# Enter numbers until 0 is entered.

strA = ' '
strInput = 0
boolLoop = True

while boolLoop:
    strInput = int(input('Give me a number (Enter 0 to stop): '))
    if strInput == 0:
        break
    else:
        strA = strA + str(strInput)

print('You entered: ', strA)
