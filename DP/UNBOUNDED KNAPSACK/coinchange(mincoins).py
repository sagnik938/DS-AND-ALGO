import sys

infy=sys.maxsize-1
coins=[2,3,8]
change=8

mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,change):
    global mat
    for i in range(n+1):
        for j in range(change+1):
            if(i==0):
                mat[i][j]=infy
            if(j==0):
                mat[i][j]=0

            if(i==1):
                if(j%coins[0] == 0):
                    mat[i][j] = j//coins[0]
                else:
                    mat[i][j] = infy

def disp(n,change):
    for i in range(n+1):
        for j in range(change+1):
            print(mat[i][j],end="\t")
        print("\n")

def coin_change_min(n,change):
    global mat
    for i in range(2,n+1):
        for j in range(1,change+1):
            if( coins[i-1] <= j ):
                mat[i][j] = min( (1 + mat[i][j-coins[i-1]]) , (mat[i-1][j]) )
            else:
                mat[i][j] = mat[i-1][j]
    return( mat[n][change] )

n=len(coins)
init(n,change)
disp(n,change)
print("Answer is " , coin_change_min(n,change) ,"\n\n")
disp(n,change)

    