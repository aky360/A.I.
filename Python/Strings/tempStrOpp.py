
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
# print(''.join(s))

a =['']*len(s)
print('a ',a)
print(s[:-1])

Str = "string"
print('str IND ',Str[Str.index('s')])
print('he he ',Str[:-1][Str.index('s')])
print(Str.index('g'))

print(chr(ord('a')-32))



ax = [('xbnnskd', 100), ('geek', 50), ('ram', 10), ('a', 5)]
print(ax)                                                      #[('xbnnskd', 100), ('geek', 50), ('ram', 10), ('a', 5)]
ax.sort(key=lambda a:a[0])
print(ax)                                                      #[('a', 5), ('geek', 50), ('ram', 10), ('xbnnskd', 100)]
ax.sort(key=lambda a:a[1])
print(ax)                                                      #[('a', 5), ('ram', 10), ('geek', 50), ('xbnnskd', 100)]


Strs = 'aeiouAEIOU'
ll = list('aeiouAEIOU')
print(ll)
strList = Strs.split()
print(strList)

atx = list(Strs)
print(atx)
atx.remove(atx[0])
print(atx)
print(''.join(atx))

sm = "small"
vowels=['a','e','i','o','u','y']
print(vowels[::])
ss=list(sm)
li=ss[::]
print()
print(ss[::])
print(li)


def Sandwiched_Vowel(s):
    vowels=['a','e','i','o','u']
    s=list(s)
    li=s[::]
    for i in range(1,len(s)-1):
        if s[i-1] not in vowels and s[i+1] not in vowels and s[i] in vowels: 
            li[i]=0
            print('li ele ', li)
    li=[x for x in li if x!=0]
    print('li ', li)
    return "".join(li)
    
print(Sandwiched_Vowel('ceghij'))   #cghj
print('a'<'z')

stt = 'ABACD'
stt1='CDABA'
temp=stt+stt1
q1 = []
for i in range(len(stt)): 
    q1.insert(0, stt[i])                      # ['A']
    print(q1)                                 # ['B', 'A']
                                              # ['A', 'B', 'A']
                                              # ['C', 'A', 'B', 'A'] /n ['D', 'C', 'A', 'B', 'A'] /n ['D', 'C', 'A', 'B', 'A']

print(q1)
print(temp.count(stt1))
