string = "studytonight"
to_array = [char for char in string]
print(to_array)                             # ['s', 't', 'u', 'd', 'y', 't', 'o', 'n', 'i', 'g', 'h', 't']


string = "studytonight"
to_array = list(string)
print(to_array)                             # ['s', 't', 'u', 'd', 'y', 't', 'o', 'n', 'i', 'g', 'h', 't']


string = "studytonight"
#empty string
to_array = []
for x in string:
    to_array.extend(x)

print(to_array)                             # ['s', 't', 'u', 'd', 'y', 't', 'o', 'n', 'i', 'g', 'h', 't']


string = "studytonight"
to_array = [*string]
print(to_array)                             # ['s', 't', 'u', 'd', 'y', 't', 'o', 'n', 'i', 'g', 'h', 't']



string = 'geeksforgeeks'
lst = []
for letter in string:
    lst.append(letter)
print(lst)                                  # ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']



def split(word):
    return list(word)

word = 'geeks'
print(split(word))                          # ['g', 'e', 'e', 'k', 's']
