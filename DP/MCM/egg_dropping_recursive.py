import sys

def solve( e , f):
    if(e==0):
        return("Invalid")
    if( e==1 ):
        return(f)
    if( f==0 or f==1):
        return(f)
    mn = sys.maxsize
    for k in range(1,f+1):
        temp_ans = 1 + max( solve(e-1,k-1) , solve(e,f-k) )
        mn = min(temp_ans,mn)
    return(mn)

e = int(input())
f = int(input())
print( solve(e,f) )
