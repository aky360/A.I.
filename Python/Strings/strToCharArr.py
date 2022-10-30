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
