#Find the sum of all prime numbers from 1 to 2 million

a = []

def isPrime(num):
   for i in xrange(2, num):
      if(num % i == 0):
         return False
   return True

counter = 17

for i in range (1,2000000):
   if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
      continue
      
   if isPrime(i):
      print i
      counter+=i

print counter


