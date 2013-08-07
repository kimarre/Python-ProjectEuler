# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

firstSum = 0
for i in range(1,101):
   firstSum = firstSum + i**2

secondSum = 0
for j in range (1,101):
   secondSum = secondSum + j

secondSum = secondSum ** 2

print firstSum, secondSum
print str(secondSum - firstSum)
