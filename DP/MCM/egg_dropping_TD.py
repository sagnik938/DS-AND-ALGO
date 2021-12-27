import sys
infy = sys.maxsize-1

mat = [[-1 for i in range(1000)]for j in range(1000)]

def init( e , f ):
    for i in range(e+1):
        for j in  range(f+1):
            if( j==0 or j==1 ):
                mat[i][j] = j
            if( i==0 ):
                mat[i][j] = infy
            if( i==1 ):
                mat[i][j] = j

def disp( e , f ):
    for i in range(e+1):
        for j in range(f+1):
            if( mat[i][j] == infy):
                print( "infy",end="\t" )
            else:
                print(mat[i][j],end="\t")
        print()

def solve( e , f ):
    for i in range(2,e+1):
        for j in range(2,f+1):

            mat[i][j] = infy
            for k in range(1,j+1):
                temp_ans = 1 + max( mat[i-1][k-1] , mat[i][j-k])
                mat[i][j] = min( mat[i][j] , temp_ans )
    return( mat[e][f] )


e=3
f=6
init(e,f)
print(solve(e,f))
#disp(e,f)