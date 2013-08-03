'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# 2 3  5 7 11 13 17 19

maxMultiple = 2*3*5*7*11*13*17*19

def isDivByAll(num):
   isDiv = True
   for i in range(1, 21):
      if not ( num % i == 0):
         isDiv = False
   return isDiv

current = 1
next = 2

isDiv = isDivByAll(current)

while not isDiv:
   current = current+2
   isDiv = isDivByAll(current)

print current





