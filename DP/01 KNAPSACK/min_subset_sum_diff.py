arr = [5,11,1,5]
mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,S):
    global mat
    for i in range(n+1):
        for j in range(S+1):
            if( i==0 ):
                mat[i][j] = False
            if( j==0 ):
                mat[i][j] = True

def disp(n,S):
    for i in range(n+1):
        for j in range(S+1):
            print(mat[i][j],end="\t")
        print()

def subsetsum(n,S):
    global mat
    for i in range(1,n+1):
        for j in range(1,S+1):
            if( arr[i-1] <= j ):
                mat[i][j] = mat[i-1][j-arr[i-1]] or mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    #return( mat[n][S] )

def min_subsetsum_diff(n,S):
    subsetsum(n,S)
    for i in range( S//2 , 0 , -1):
        if( mat[n][i] ):
            break
    return( S - 2*i )

n = len(arr)
S = sum(arr)
init(n,S)
print(min_subsetsum_diff(n,S))
disp(n,S)

