def setrowzero(matrix):
    m=len(matrix)
    n=len(matrix[0])
    xoffset=[]
    yoffset=[]
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j]==0:
                if i not in xoffset:
                    xoffset.append(i)
                if j not in yoffset:
                    yoffset.append(j)

    for i in range(0,m):
        for j in range(0,n):
            if i in xoffset or j in yoffset:
                matrix[i][j]=0

    return matrix

matrix=[[1,2,3],[4,0,6],[7,8,9]]
print setrowzero(matrix)