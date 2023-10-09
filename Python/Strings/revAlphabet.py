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


class Solution:
    def reciprocalString(self, S):
        dicS, dicL, ans = {}, {}, ""
        for i in range(26):
            dicL[chr(65+i)] = chr(90-i)
            dicS[chr(97+i)] = chr(122-i)
        for val in S:
            if val!=' ':
                if val in dicS.keys(): ans += dicS.get(val)
                if val in dicL.keys(): ans += dicL.get(val)
            else: ans += " "
        return ans

class Solution:
    def reciprocalString(self, S):
        dicS, dicL, ans = {}, {}, ""
        for i in range(26):
            dicL[chr(65+i)] = chr(90-i)
            dicS[chr(97+i)] = chr(122-i)
        for val in S:
            if val in dicS.keys(): ans += dicS.get(val)
            elif val in dicL.keys(): ans += dicL.get(val)
            else: ans += val
        return ans


class Solution:
    def reciprocalString(self, S):
        ans=""
        for x in S:
            if x>='A' and x<='Z': ans+=chr(90-(ord(x)-65))
            elif x>='a' and x<='z': ans+=chr(122-(ord(x)-97))
            else: ans+=x
        return ans



class Solution:
    def reciprocalString(self, S):
        tmp1='abcdefghijklmnopqrstuvwxyz'
        tmp2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        x=''
        for i in S:
            if i in tmp1: x+=tmp1[::-1][tmp1.index(i)]
            elif i in tmp2: x+=tmp2[::-1][tmp2.index(i)]
            else: x+=i
        return x
