length=8
prof=[2,4,6,1,4,8,3,9]
cuts=[i+1 for i in range(length)]

mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,length):
    global mat
    for i in range(n+1):
        for j in range(length+1):
            if(i==0 or j==0):
                mat[i][j]=0

def disp(n,length):
    for i in range(n+1):
        for j in range(length+1):
            print(mat[i][j],end="\t")
        print("\n")

def rodcutter(n,length):
    global mat
    for i in range(1,n+1):
        for j in range(1,length+1):
            if( cuts[i-1]<=j ):
                mat[i][j] = max ( (prof[i-1] + mat[i][j-cuts[i-1]]) , (mat[i-1][j]) )
            else:
                mat[i][j] = mat[i-1][j]
    return( mat[n][length] )

n=len(cuts)
init(n,length)
disp(n,length)
print(rodcutter(n,length))
disp(n,length)