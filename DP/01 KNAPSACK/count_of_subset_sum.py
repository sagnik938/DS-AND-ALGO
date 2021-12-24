arr=[1,2,3,4,5,6,7,8]
mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,sum):
    global mat
    for i in range(n+1):
        for j in range(sum+1):
            if(i==0):
                mat[i][j]=0
            if(j==0):
                mat[i][j]=1

def disp(n,sum):
    for i in range(n+1):
        for j in range(sum+1):
            print(mat[i][j],end="\t")
        print("\n")

def count_SS(n,sum):
    global mat
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if( arr[i-1] <= j ):
                mat[i][j] = mat[i-1][j-arr[i-1]] + mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    return(mat[n][sum])

sum=3
n=len(arr)
init(n,sum)
disp(n,sum)
print("Answer is ",count_SS(n,sum),"\n\n")
disp(n,sum)


