#max no of ways
change=8
coins=[1,3,5]
mat=[[-1 for i in range(1000)]for j in range(1000)]

def init1(n,change):
    global mat
    for i in range(n+1):
        for j in range(change+1):
            if( i==0 ):
                mat[i][j]=0
            if(j==0):
                mat[i][j]=1

def disp(n,change):
    for i in range(n+1):
        for j in range(change+1):
            print(mat[i][j],end="\t")
        print("\n")

def coin_change_max_ways(n,change):
    global mat
    for i in range(1,n+1):
        for j in range(1,change+1):
            if( coins[i-1]<=j ):
                mat[i][j] = (mat[i][j-coins[i-1]]) + (mat[i-1][j]) 
            else:
                mat[i][j] = mat[i-1][j]
    return(mat[n][change])

n=len(coins)
init1(n,change)
disp(n,change)
print(coin_change_max_ways(n,change))
disp(n,change)
