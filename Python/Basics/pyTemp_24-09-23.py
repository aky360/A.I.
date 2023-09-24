a = '1301'
bins = ['0', '1']

gf = "dgfg"
print('len str ', len(gf))
print()

names = ["Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks"]
  
for i, v in enumerate(names):
    print(i, v)

print(' a b '[::-1])

num = 234
num //= 10
print(num)

x = 200
print(x%10)

for i in a:
    if i not in bins:
        print("NO")
        
        
def reverse_digit(n):
    # Code here
    rev, num = 0, n
    while(num<0):
        remainder = num%10
        rev = rev*10 + remainder
        num //= 10
        print(rev)
		
    return rev
    
print()
print(reverse_digit(2234))
        
def isBinary(str):
    return str.count('0') + str.count('1') == len(str)
    
    
print(isBinary(a))
