prof = [3,4]
wt = [1,4]

mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,W):
    global mat
    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0):
                mat[i][j]=0

def disp(n,W):
    for i in range(n+1):
        for j in range(W+1):
            print(mat[i][j],end="\t")
        print("\n")

def uknaptd(n,W):
    global mat
    for i in range(1,n+1):
        for j in range(1,W+1):
            if( wt[i-1]<=j ):
                mat[i][j] = max ( (prof[i-1] + mat[i][j-wt[i-1]]) , (mat[i-1][j]) )
            else:
                mat[i][j] = mat[i-1][j]
    return( mat[n][W] )

n=len(wt)
W=6
init(n,W)
disp(n,W)
print(uknaptd(n,W))
disp(n,W)
