x=float(123)
print(x)	#123.0	as value is cast to float

x=float('123')
print(x)	#123.0 as the value is cast to float

x=float('123.23')
print(x)	#123.23 as value is cast to float

x=int(123.23)
print(x)	#123 as value is cast to int

#x=int('123.23')
#print(x)	ValueError: invalid literal for int() with base 10: '123.23'

x=int(float('123.23'))
print(x)	#123 as the value is cast to int

x=str(12)
print(x)	#12 as it is cast to string

x=str(12.2)
print(x)	#12.2

x=bool('a')
print(x)	#True 

x=bool(0)
print(x)	#False as 0 = false

x=bool(0.1)
print(x)	#True as any value which isn't 0 is true