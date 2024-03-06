
def grid_transforms(T, inst):
    output = []
    cols = len(T[0])
    rows  = len(T)
    for i in range(len(inst)):
        if inst[i] == 'CW':
            grid_cw = [[0]*rows for _ in range(cols)]
            for c in range(cols):
                for r in range(rows-1,-1,-1):
                    grid_cw[c][rows-r-1] = T[r][c]
            output.append(grid_cw)
            
        elif inst[i] == 'CCW':
            grid_ccw = [[0]*rows for _ in range(cols)]
            for c in range(cols-1,-1,-1):
                for r in range(rows):
                    grid_ccw[cols-c-1][r] = T[r][c]
            output.append(grid_ccw)
        elif inst[i] == 'FLIP_V':
            grid_v = [[0]*cols for _ in range(rows)]
            
            output.append(grid_v)
    return output
print(grid_transforms([
        [11, 12, 21, 22],
        [98, 89, 99, 88],
        [73, 37, 33, 77],
    ],['FLIP_V']))
'''

X = [[9, 8, 7, 9], [6, 5, 4, 9], [3, 2, 1, 9]]
 
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
 
for row in range(len(X)):
    for column in range(len(X[0])):
        result[column][row] = X[row][column]
 
for r in result:
    print(r)
     
# # Python Program to Transpose a Matrix using the list comprehension
 
# rez = [[X[column][row] for column in range(len(X))] 
#    for row in range(len(X[0]))]
 
# for row in rez:
#     print(row)
    '''