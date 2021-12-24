prof = [3,4,5,6,1,2]
wt = [3,3,3,6,7,9]

mat=[[-1 for i in range(1000)]for j in range(1000)]

def knapsack( n , W ):
    if(n==0 or W==0):
        return(0)

    if(mat[n][W]!=-1):
        return( mat[n][W] )
    
    if( wt[n-1] <= W ):
        mat[n][W] = max( (prof[n-1] + knapsack(n-1,W-wt[n-1])) , (knapsack( n-1 , W)) )
        return( mat[n][W] )
    else:
        mat[n][W] = knapsack( n-1,W )
        return( mat[n][W] )

W=10
n=len(wt)
print(knapsack(n,W))

