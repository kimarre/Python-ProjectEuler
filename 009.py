
#Find three numbers for which a+b+c=1000 and a^2+b^2=c^2

def pythagorean(a, b, c):
   return a**2 + b**2 == c**2

found = False
product = 0

for a in range(1,1001):
   for b in range(1,1001):
      for c in range(1,1001):
         if a + b + c == 1000 and a**2+b**2 == c**2:
            product =  a*b*c
            print "a: " + str(a)
            print "b: " + str(b)
            print "c: " + str(c)
            found = True
      if found == True:
         break
   if found == True:
      break

print product


