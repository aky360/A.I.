arr = [1,2,334,4,5]

print(type({*arr}))               # <class 'set'>
print(*arr)                       # 1 2 334 4 5

print(type([*arr]))                # <class 'list'>
print(*arr)                        # 1 2 334 4 5

print(type((*arr,)))               # <class 'tuple'>
print(*arr)                        # 1 2 334 4 5

dic = {}
for i, num in enumerate(arr):
    print(i,"=>",num)                    # 0 => 1, 1 => 2, 2 => 334, 3 => 4, 4 => 5
    dic[i] = num
    
    
print([*dic.values()])                           # [1, 2, 334, 4, 5]
print([*dic.keys()])                             # [0, 1, 2, 3, 4]

print((*dic.values(),))                          # (1, 2, 334, 4, 5)
print((*dic.keys(),))                            # (0, 1, 2, 3, 4)

print({*dic.values()})                           # {1, 2, 4, 5, 334}
print({"2" : {*dic.keys()}})                     # {'2': {0, 1, 2, 3, 4}}
    
tp ={'1' : [*arr]}
print(type(tp))                                  # <class 'dict'>
print(*arr)                                      # 1 2 334 4 5
