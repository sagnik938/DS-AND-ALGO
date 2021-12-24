#target sum also

arr = [5,11,1,5]
mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,S):
    global mat
    for i in range(n+1):
        for j in range(S+1):
            if( i==0 ):
                mat[i][j] = 0
            if( j==0 ):
                mat[i][j] = 1

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
                mat[i][j] = mat[i-1][j-arr[i-1]] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    return( mat[n][S] )

def constant_subsetsum_diff(n,S,k):
    if(k>S):
        return("Invalid")
    else:
        return(subsetsum(n,(S+k)//2))
    
n = len(arr)
S = sum(arr)
k = 0
init(n,S)
print(constant_subsetsum_diff(n,S,k))
disp(n,S)

