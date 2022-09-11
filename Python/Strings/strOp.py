string = "PrOgRaMMing is the fun "

print(string.lower())                                          # programming is the fun 
print(string.upper())                                          # PROGRAMMING IS THE FUN


string = "This will split all words into a list"

print(string.split())                                           # ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

string = "This will split all words into a list"
list_a = string.split()
print(list_a)                                                   # ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

x = ' '.join(list_a)                                            # 
y = ', '.join(list_a)                                           #
z = ' :'.join(list_a)                                           #

print(x)                                                        # This will split all words into a list
print(y)                                                        # This, will, split, all, words, into, a, list
print(z)                                                        # This :will :split :all :words :into :a :list


string = 'Happy New Year'          
print(string)                                                   # Happy New Year
print(string.find('ew'))                                        # 7

print(string.replace('Happy','Brilliant'))                      # Brilliant New Year
