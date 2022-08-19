arr = [1,2,334,4,5]

print(type({*arr}))
print(*arr)

print(type([*arr]))
print(*arr)

print(type((*arr,)))
print(*arr)

dic = {}
for i, num in enumerate(arr):
    print(i,"=>",num)
    dic[i] = num
    
    
print([*dic.values()])
print([*dic.keys()])

print((*dic.values(),))
print((*dic.keys(),))

print({*dic.values()})
print({"2" : {*dic.keys()}})
    
tp ={'1' : [*arr]}
print(type(tp))
print(*arr)
