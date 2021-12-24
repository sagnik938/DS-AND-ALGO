prof = [3,4,5,6,1,3,4]
wt = [1,4,2,3,7,5,1]

def uknap(n,W):
    if(n==0 or W==0):
        return 0
    if( wt[n-1]<= W):
        return( max( (prof[n-1] + uknap(n,W-wt[n-1])) , (uknap(n-1,W)) ) )
    else:
        return( uknap(n-1,W) )

n=len(wt)
W=10
print(uknap(n,W))