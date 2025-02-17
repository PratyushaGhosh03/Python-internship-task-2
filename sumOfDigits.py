#Sum of digits
num=int(input('Enter a number:'))
sum=0
while(num!=0):
  dig=num%10
  sum+=dig
  num=num//10
print('Sum of digits of numberr is:',sum)
