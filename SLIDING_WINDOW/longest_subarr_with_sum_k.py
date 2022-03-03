def solve(arr,n,k):
    i = j = 0
    localsum = mxsize = 0
    while( j < n ):
        localsum += arr[j]
        if( localsum < k ):
            j += 1
        elif( localsum == k):
            mxsize = max(mxsize,(j-i+1))
            j += 1
        elif( localsum > k):
            while(localsum > k):
                localsum -= arr[i]
                i += 1
            j += 1
    return(mxsize)

arr = [4,1,1,1,2,1,1,1,1,1]
k = 5
print(solve(arr,len(arr),k))