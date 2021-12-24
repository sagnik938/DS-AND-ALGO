x="uagbcba"
y="".join(reversed(x))

mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n):
    global mat
    for i in range(n+1):
        for j in range(n+1):
            if(i==0 or j==0):
                mat[i][j]=0

def disp(n):
    for i in range(n+1):
        for j in range(n+1):
            print(mat[i][j],end="\t")
        print("\n")

def lps(n):
    global mat
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(x[i-1]==y[j-1]):
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max( (mat[i-1][j]) , (mat[i][j-1]) )
    return(mat[n][n])

def insertiondeletion(n):
    l=lps(n)
    return(n-l)


n=len(x)

init(n)
disp(n)
print("INS/DEL ",insertiondeletion(n))
disp(n)