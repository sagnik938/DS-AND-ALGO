prof = [3,4,5,6,1,3,4]
wt = [1,4,2,3,7,5,1]

mat=[[-1 for i in range(1000)]for j in range(1000)]

def uknap(n,W):
    global mat
    if(n==0 or W==0):
        return 0

    if(mat[n][W]!=-1):
        return( mat[n][W] )

    if( wt[n-1]<= W):
        mat[n][W] = max( (prof[n-1] + uknap(n,W-wt[n-1])) , (uknap(n-1,W)) ) 
        return( mat[n][W] )

    else:
        mat[n][W] = ( uknap(n-1,W) )
        return( mat[n][W] )

n=len(wt)
W=10
print(uknap(n,W))