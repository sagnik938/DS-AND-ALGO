def solve(arr,n):
    dp = [1]
    ans = 0
    for i in range(1,n):
        maxlen = 0
        for j in range(0,i):
            if( arr[i] > arr[j] ):
                maxlen = max(maxlen,dp[j])
        dp.append(maxlen + 1)
        ans = max(ans,dp[i])
    print(dp)
    return(ans)

arr = [5,7,8,1,9,1,2,3,4,5,9,12]
print(solve(arr,len(arr)))
