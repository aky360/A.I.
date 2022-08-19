import ctypes
val = [90, 1,2,3]
myiter = iter(val)

print('next iterator value is ', next(myiter))
print('next iterator value is ', next(myiter))
print('next iterator value is ', next(myiter))
print('next iterator value is ', next(myiter))

print('address of val list ', id(val), ctypes.cast(id(val), ctypes.py_object).value)

ids = id(val[0])

for i, num in enumerate(val):
    print('address of ', i, id(num))
    print('value at address ', i, ctypes.cast(id(num), ctypes.py_object).value)

print('val[0] addresss ' , id(val[0]))
c = ctypes.cast(ids, ctypes.py_object).value
print('value at val[0] ', c)

# print(next(myit), id(next(myit)))
# print(next(myit), id(next(myit)))
# print(next(myit), id(next(myit)))
# print(next(myit), id(next(myit)))


print('address of val ', id(val), ctypes.cast(id(val), ctypes.py_object).value)
print(id(90))

print(id(90+1))

print(id(90+2))
print(id(90+3))

print(id(90+4))

print(id(90+5))


ar = [1,2,3,4]
arr = [1,2,3,4]
y = id(arr)
x = id(ar)

print("Memory address - ", x)
print("Memory address - ", y)

a = ctypes.cast(x, ctypes.py_object).value
b = ctypes.cast(y, ctypes.py_object).value
print('value at x ', a)
print('value at y ', b)
