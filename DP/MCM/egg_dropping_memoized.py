import sys

mat = [[-1 for i in range(1000)]for j in range(1000)]

def solve( e , f):
    if(e==0):
        return("Invalid")
    if( e==1 ):
        return(f)
    if( f==0 or f==1):
        return(f)

    if( mat[e][f]!=-1 ):
        return(mat[e][f])

    mn = sys.maxsize
    for k in range(1,f+1):
        temp_ans = 1 + max( solve(e-1,k-1) , solve(e,f-k) )
        mn = min(temp_ans,mn)
    mat[e][f]=mn
    return(mat[e][f])

e = int(input())
f = int(input())
print( solve(e,f) )
