def solve(arr,n):
    dp = ["$" for i in range(n)]
    if(n==0):
        return(0)
    if(n==1):
        return(arr[0])
    dp[0] = max(0,arr[0])
    dp[1] = max(dp[0],arr[1])
    for i in range(2,n):
        dp[i] = max( dp[i-1],arr[i]+dp[i-2] )
    print(dp)
    return(dp[n-1])

arr = [3,7,4,6,5]
solve(arr,len(arr))