#Problem 3

'''Pseudocode:
for values 2-10 
    if the values are divisible by i
        num = num/i

'''
currentNum = 600851475143
half = 600851475143/2
highest = 0

for i in xrange(2, half):
   if currentNum % i == 0:
      currentNum = currentNum/i
      highest = i
   if currentNum <= 1:
      break

if currentNum > highest:
   print currentNum
else:
   print highest


'''highRange = 600851475143/2

for i in range (2,highRange):
   if 
'''

