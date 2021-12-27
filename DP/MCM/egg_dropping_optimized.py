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

        #optimisation
        if( mat[e-1][k-1]!=-1 ):
            t1 = mat[e-1][k-1]
        else:
            t1 = solve(e-1,k-1)

        if( mat[e][f-k]!=-1 ):
            t2 = mat[e][f-k]
        else:
            t2 = solve(e,f-k)

        temp_ans = 1 + max( t1,t2 )
        mn = min(temp_ans,mn)
    mat[e][f]=mn
    return(mat[e][f])

e = int(input())
f = int(input())
print( solve(e,f) )
