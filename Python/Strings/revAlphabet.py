"""
Program to print reciprocal of letters.
"""

tmp1='abcdefghijklmnopqrstuvwxyz'
tmp2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

x=''
S = 'ab C xyz'
print(S[::-1])                        #'zyx C ba'
print(S[S.index('a')])                #'a'
print(S[::-1][S.index('a')])          #'z'
for i in S:
    if i in tmp1:
        x+=tmp1[::-1][tmp1.index(i)]
    elif i in tmp2: 
        x+=tmp2[::-1][tmp2.index(i)]
    else: 
        x+=i


print(x)         #zy X cba
