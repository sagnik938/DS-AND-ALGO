x="geeks"
y="eke"
res=""

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

def printscs(n,m):
    lcs(n,m)
    global res
    i=n
    j=m
    while(i>0 and j>0):
        if(x[i-1]==y[j-1]):
           res+=x[i-1]
           i-=1
           j-=1
        elif(mat[i-1][j]>=mat[i][j-1]):
            res+=x[i-1]
            i-=1
        elif(mat[i][j-1]>mat[i-1][j]):
            res+=y[j-1]
            j-=1
    
    while(i>0):
        res+=x[i-1]
        i-=1
    while(j>0):
        res+=y[j-1]
        j-=1
    return ("".join(reversed(res)))

n=len(x)
m=len(y)

init(n,m)
disp(n,m)
print(printscs(n,m))
disp(n,m)