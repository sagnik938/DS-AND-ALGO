x="aaa"
y="baaa"

mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,m):
    global mat
    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                mat[i][j]=0

def disp(n,m):
    for i in range(n+1):
        for j in range(m+1):
            print(mat[i][j],end="\t")
        print("\n")

def lcs(n,m):
    global mat
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(x[i-1]==y[j-1]):
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max( (mat[i-1][j]) , (mat[i][j-1]) )
    return(mat[n][m])

def match(n,m):
    if( lcs(n,m) == min(n,m) ):
        return( True)
    else:
        return( False )

n=len(x)
m=len(y)

init(n,m)
disp(n,m)
print(match(n,m))
disp(n,m)