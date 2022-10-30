matrix = [[1,2,3],[3,1,2],[2,3,1]]
row, col =len(matrix), len(matrix[0])

mat = [[1,1,1],[2,2,2],[3,3,3]]
print(str(matrix[0]))

for i in zip(mat):
    print(i)

for i in zip(zip(*matrix)):
    print(i)

for i in zip(mat, zip(*matrix)):
    print(i)

for i, z in zip(mat, zip(*matrix)):
    print(i, z)


for row, col in zip(matrix, zip(*matrix)):
    print(row, col)
    
    
    
"""
[1, 2, 3]
([1, 1, 1],)
([2, 2, 2],)
([3, 3, 3],)
((1, 3, 2),)
((2, 1, 3),)
((3, 2, 1),)
([1, 1, 1], (1, 3, 2))
([2, 2, 2], (2, 1, 3))
([3, 3, 3], (3, 2, 1))
[1, 1, 1] (1, 3, 2)
[2, 2, 2] (2, 1, 3)
[3, 3, 3] (3, 2, 1)
[1, 2, 3] (1, 3, 2)
[3, 1, 2] (2, 1, 3)
[2, 3, 1] (3, 2, 1)
"""
