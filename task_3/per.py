import random 
matrix = []

for i in range (n):
    matrix.append ([])
    for j in range (n):
        matrix[i].append (random.randint (0, 20))

print (matrix)