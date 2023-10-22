

l=int(ord('z'))
t=int(ord('a'))
j=l-t
print(l, t, j)
print(chr(25))

print(chr(ord('z')-ord('b')+ord('a')))


s = ['s','t','r','i']
print('ssR s ',s[:-1])
print(s)
print('s ', s[:-0])
del s[3]
print(s)
s.remove(s[2])
print(s)
print(''.join(s))

a =['']*len(s)
print('a ',a)
print(s[:-1])

Str = "string"
print('str IND ',Str[Str.index('s')])
print('he he ',Str[:-1][Str.index('s')])
print(Str.index('g'))

print(chr(ord('a')-32))
