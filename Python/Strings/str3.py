x = 'a'
print('x ', x.isalpha())                                         # True


name = "Monica"
print(name.isalpha())                                            # True

# contains whitespace
name = "Monica Geller"
print(name.isalpha())                                            # True

# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())                                            # False


c = 'p'
print(ord(c))                                                    # 112

print(chr(ord(c))                                                # p
print(chr(112))                                                  # p
      
print(chr(65))                                                   # 'A'
print(chr(120))                                                  # 'x'
print(chr(ord('S') + 1))                                         # 'T'
