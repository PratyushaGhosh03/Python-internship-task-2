#Count vowels and consonents
s=str(input('Enter a String:'))
v=0
for ch in s:
  if ch in 'aeiouAEIOU':
      v=v+1
print('Total vowel in',s,'is:',v)
