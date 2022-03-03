def max_sum(arr,n,k):
    i = j = 0;
    curr_sum = max_sum = 0
    while(j<n):
        curr_sum += arr[j]
        if(j-i+1 < k):
            j += 1
        else:
            maxsum = max(curr_sum,max_sum)
            curr_sum -= arr[i]
            i += 1
            j += 1
    return(maxsum)

arr = [100,200,300,400]
k = 2
n = len(arr)
print(max_sum(arr,n,k))
