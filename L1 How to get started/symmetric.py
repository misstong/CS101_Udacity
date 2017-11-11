def symmetric(list):
    # Your code here
    if(len(list)==0):
        return True;
    if(len(list)!=len(list[0])):
        return False;
    for i in range(0,len(list)):
        for j in range(0,len(list[0])):
            if(list[i][j]!=list[j][i]):
                return False;
    return True;

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
print symmetric([[1,2,3]])
print symmetric([])
