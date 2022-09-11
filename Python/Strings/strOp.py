string = "PrOgRaMMing is the fun "

print(string.lower())
print(string.upper())


string = "This will split all words into a list"

print(string.split())

string = "This will split all words into a list"
list_a = string.split()
print(list_a)

x = ' '.join(list_a)
y = ', '.join(list_a)
z = ' :'.join(list_a)

print(x)
print(y)
print(z)


string = 'Happy New Year'
print(string.find('ew'))

print(string.replace('Happy','Brilliant'))
