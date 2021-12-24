arr=[1,2,5]
mat=[[-1 for i in range(1000)]for j in range(1000)]

def init(n,sum):
    global mat
    for i in range(n+1):
        for j in range(sum+1):
            if(i==0):
                mat[i][j]=False
            if(j==0):
                mat[i][j]=True

def disp(n,sum):
    for i in range(n+1):
        for j in range(sum+1):
            print(mat[i][j],end="\t")
        print("\n")

def summation(n):
    sum=0
    for i in range(n):
        sum+=arr[i]
    return(sum)

def subset_sum(n,sum):
    global mat
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if( arr[i-1] <= j ):
                mat[i][j] = mat[i-1][j-arr[i-1]] or mat[i-1][j]
            else:
                mat[i][j] = mat[i-1][j]
    return(mat[n][sum])

def eqs(n,sum):
    if(sum%2!=0):
        return(False)
    else:
        return(subset_sum(n,sum//2))
    

n=len(arr)
sum=summation(n)
init(n,sum)
disp(n,sum)
print("Answer is ",eqs(n,sum),"\n\n")
disp(n,sum)