#lcm and gcd
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))

if(x>y):
 smaller=y
else:
 smaller=x
for i in range(1,smaller+1):
  if((x%i==0)and(y%i==0)):
    gcd=i
lcm=(x*y)/gcd
print('The gcd of',x,'and',y,'is',gcd)
print('The lcm of',x,'and',y,'is',lcm)
