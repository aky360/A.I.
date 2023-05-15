
num = [1,2,34,5,66,7,88]

# List of tuples
num_con = [(i, v) for i, v in enumerate(num)]
print(num_con)                                                                              # [(0, 1), (1, 2), (2, 34), (3, 5), (4, 66), (5, 7), (6, 88)]
print(num_con[0][0])                                                                        # 0
print(num_con[len(num)-1][0])                                                               # 6

# dictionary 
num_cons = {i:v for i, v in enumerate(num)}
print(num_cons)                                                                             # {0: 1, 1: 2, 2: 34, 3: 5, 4: 66, 5: 7, 6: 88}
print(num_cons.keys)                                                                        # <built-in method keys of dict object at 0x7f450f2ddcc0>
print(num_cons.keys, ' => ',num_cons.keys(), ' => ', type(num_cons.keys()))                 # <built-in method keys of dict object at 0x7f450f2ddcc0>  =>  dict_keys([0, 1, 2, 3, 4, 5, 6])  =>  <class 'dict_keys'>
print(num_cons.keys, ' => ',*num_cons.keys())                                               # <built-in method keys of dict object at 0x7f450f2ddcc0>  =>  0 1 2 3 4 5 6
print(num_cons.keys, ' => ',[*num_cons.keys()], ' => ', type([*num_cons.keys()]))           # <built-in method keys of dict object at 0x7f450f2ddcc0>  =>  [0, 1, 2, 3, 4, 5, 6]  =>  <class 'list'>
print(num_cons.keys, ' => ',(*num_cons.keys(),), ' => ', type((*num_cons.keys(),)))         # <built-in method keys of dict object at 0x7f450f2ddcc0>  =>  (0, 1, 2, 3, 4, 5, 6)  =>  <class 'tuple'>
print(num_cons.keys, ' => ',{*num_cons.keys()}, ' => ', type({*num_cons.keys()}))           # <built-in method keys of dict object at 0x7f450f2ddcc0>  =>  {0, 1, 2, 3, 4, 5, 6}  =>  <class 'set'>
print(num_cons.values)                                                                      # <built-in method values of dict object at 0x7f450f2ddcc0>
print(num_cons.values, ' => ',num_cons.values(), ' => ', type(num_cons.values()))           # <built-in method values of dict object at 0x7f450f2ddcc0>  =>  dict_values([1, 2, 34, 5, 66, 7, 88])  =>  <class 'dict_values'>
print(num_cons.values, ' => ',*num_cons.values())                                           # <built-in method values of dict object at 0x7f450f2ddcc0>  =>  1 2 34 5 66 7 88
print(num_cons.values, ' => ',[*num_cons.values()], ' => ', type([*num_cons.values()]))     # <built-in method values of dict object at 0x7f450f2ddcc0>  =>  [1, 2, 34, 5, 66, 7, 88]  =>  <class 'list'>
print(num_cons.values, ' => ',(*num_cons.values(),), ' => ', type((*num_cons.values(),)))   # <built-in method values of dict object at 0x7f450f2ddcc0>  =>  (1, 2, 34, 5, 66, 7, 88)  =>  <class 'tuple'>
print(num_cons.values, ' => ',{*num_cons.values()}, ' => ', type({*num_cons.values()}))     # <built-in method values of dict object at 0x7f450f2ddcc0>  =>  {1, 2, 66, 34, 5, 7, 88}  =>  <class 'set'>

print('type of of keys ', type(num_cons.keys()))                                            # type of of keys  <class 'dict_keys'>
print('type of of keys ', type([*num_cons.keys()]))                                         # type of of keys  <class 'list'>

print('type of of values ', type(num_cons.values()))                                        # type of of values  <class 'dict_values'>
print('type of of values ', type([*num_cons.values()]))                                     # type of of values  <class 'list'>

arr = [*num_cons.values()]
print(type(arr), ' => ', arr)                                                               # <class 'list'>  =>  [1, 2, 34, 5, 66, 7, 88]


***
find the value of dictionary from key using get method
***

x = {'a':1, 'b':2, 'c':'x'}
print('value ', x.get('a', 0))                                                              # count 1
print('value ', x.get('b', 0))                                                              # count 2
print('value ', x.get('c', 0))                                                              # count x
print('value ', x.get('d', 0))                                                              # count 0
