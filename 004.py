# Problem 4 under Project Euler

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

''' PSEUDOCODE
   function to check for palindrome:
      store the reversed number
      return whether or not the original is equal to the reversed

   initialize max palindrome

   for numbers from 100 to 999
      for numbers 100 to 999
         if function returns true
            if it is larger than max palindrome
               update max palindrome

'''

def isPalindrome(original):
   reversed = str(original)[::-1]
   return reversed == str(original)

maxPalindrome = 0
temp = 0

for i in range (100, 999):
   for j in range (100, 999):
      temp = i*j
      if isPalindrome(temp):
         if temp > maxPalindrome:
            maxPalindrome = temp

print maxPalindrome


