

print(chr(65))
print(ord("A"))

dicS, dicL = {}, {}
for i in range(26):
    dicL[chr(65+i)] = chr(90-i)
    dicS[chr(97+i)] = chr(122-i)
    
    
print(dicS)
print(dicL)

if "A" in dicL.keys():
    print("yes")
    
x = 'a'
if x in dicS.keys():
    print("yes")

if "A" in dicS.keys():
    print("no")
else:
    print("Yes")
    
    
tmp1='abcdefghijklmnopqrstuvwxyz'
tmp2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

x=''
S = 'ab C xyz'
print(S[::-1][S.index('a')])
for i in S:
    if i in tmp1:
        x+=tmp1[::-1][tmp1.index(i)]
    elif i in tmp2: 
        x+=tmp2[::-1][tmp2.index(i)]
    else: 
        x+=i
    
    
print(x)

l = "GeeksforGeeks"
for i in l[::-1]:
    print(l[l.index(i)])
    
ans =""
for i in range(len(l)):
    ans+=l[::-1][l.index(l[i])]
    
print(ans)
print(l)

string = "i love programming"
ans = ""
for i in range(len(string)):
    if i!=" " and i==0:
        ans+=string[i].upper()
    elif string[i-1] == " " and string[i]!= " ":
        ans+=string[i].upper()
    else:
        ans+=string[i]
        
print(ans)
