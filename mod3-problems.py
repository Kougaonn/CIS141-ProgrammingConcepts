# String and repeat

strA = input('Input a string: ')
strMod = int(input('Times to repeat: '))

print(strA * strMod)
print('-' * 8)

# Calculate age

strA = input('What\'s your name? ')
strMod = int(input('How old are you? '))

print("Hello,", strA, "! You are", strMod, "years old. Next year you will be", strMod + 1, "years old.")
print('-' * 8)

# Find string by keyword

strA = input('Give me a sentence: ')
strB = input('Give me a word to look for: ')

print(strB in strA)
print('-' * 8)

# Word slicing

strA = input('Give me a new word:\n ')
indA = int(input('Give me an index:\n '))
indB = int(input('Give me a second index:\n '))

print(strA[indA:indB])
print('-' * 8)

# Print bars

#Input
strA = 'Oh no we\'re splitting!'
print('-' * 8)
print(strA)

#Split it
strB = strA.split(" ")
print('-' * 8)
print(strB)

#Join it
strA = '|'.join(strB)
print('-' * 8)
print(strA)
