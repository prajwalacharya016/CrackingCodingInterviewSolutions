def rotate(mylist):
    n=len(mylist)
    for layer in range(0,n/2):
        first = layer
        last = n-1-layer

        for i in range(first,last):
            offset = i - first
            top = mylist[first][i]
            mylist[first][i] = mylist[last-offset][first]
            mylist[last - offset][first]=mylist[last][last-offset]
            mylist[last][last-offset]=mylist[i][last]
            mylist[i][last]=top

    return mylist

mylist=[[1,2,3],[4,5,6],[7,8,9]]
print rotate(mylist)