# --sum the values of the fibbonacci sequence that are even--
 
# var1 = the current value, 
# var2 = last value

# while var1 isn't larger than 4 million 
#      if val1 is even
#            add it to sum
#      temp is assigned var2
#      var2 is assigned var1
#      var1 is temp + var2

var1 = 2
var2 = 1
sum = 0

while var1 < 4000000:
    if var1 % 2 == 0:
        sum += var1
    temp = var2
    var2 = var1
    var1 = temp + var2

print sum
 
