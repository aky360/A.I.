sts = {1,3,6,7,8}
dict = {1: 2, 2:3}
nDict = {3: 3, 4: 3, 12: 3, 7: 1, 11: 1, 6: 1, 5: 1}

print('sts ', sorted(sts))

for i in nDict:
    print('default key s ', i)
    
for _ in nDict.values():
    print(_)
print()

print(sorted(nDict.items()))
print()

for (key, value) in sorted(nDict.items()):
    print(key, value)
print()

for (key, value) in nDict.items():
    if value > 1:
        print(key, value)
print()
    
for i, v in enumerate(nDict.items()):
    print(i, v)
print()

print(dict.keys())
gst = [7, 6, 8, 4, 9, 8, 4, 7, 4, 4]
lst = [3, 4, 12, 3, 12, 3, 4, 4, 12, 7, 11, 6, 5]

def duplicates(arr, n):
    dict, outputArr = {}, []
    for value in arr:
        if value in dict:
            dict[value] += 1
            if value not in outputArr:
                outputArr.append(value)
        else:
            dict[value] = 1
        
    return sorted(outputArr) if outputArr else [-1]


print(duplicates(gst, 10))
