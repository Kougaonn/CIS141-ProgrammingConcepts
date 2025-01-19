# Avatar Reference Portion
print("Water. Earth. Fire. Air. Long ago, the four nations lived together in harmony. Then, everything changed when the Fire Nation attacked.")
print("---")

# Math Processing
# Input
import math
varA = int(input("Variable A "))
varB = int(input("Variable B "))

# Output
print("Subtraction: ", varA - varB)
print("Addition: ", varA + varB)
print("Multiplication: ", varA * varB)
print("Division: ", varA / varB)
print("---")

# Compute triangular area
varA = int(input("Side A "))
varB = int(input("Side B "))
varC = int(input("Side C "))
varD = (varA + varB + varC) / 2

print("Semiperimeter: ", varD)

print(math.sqrt(varD * (varD-varA) * (varD-varB) * (varD - varC)))
print("---")

# Stats
varA = int(input("Data Point A "))
varB = int(input("Data Point B "))
varC = int(input("Data Point C "))
varD = int(input("Data Point D "))
varE = int(input("Data Point E "))
listA = [varA, varB, varC, varD, varE]
varAvg = (varA + varB + varC + varD + varE) / 5

print("Total :", varA + varB + varC + varD + varE)
print("Average: ", varAvg)
print("Minimum: ", min(listA))
print("Maximum: ", max(listA))
print("Range: ", min(listA) - max(listA))
print("Standard Deviation: ", math.sqrt(((varA - varAvg) ** 2 + (varB - varAvg) ** 2 + (varC - varAvg) ** 2 + (varD - varAvg) ** 2 +(varE - varAvg) ** 2) / 4))
