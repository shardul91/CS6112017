#print(2000.3 ** 200) OverflowError: (34, 'Result too large')
print(1.0 + 1.0 - 1.0) #Output is 1.0
print(1.0 + 1.0e20 - 1.0e20) #The maximum value python is able to print is for 1.0e15. Hence the output for this is 0 as (1.0e20 + anything)=1.0e20 which is then subtracted with the same number