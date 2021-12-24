import sys

arr=[40,20,30,10,30]

def solve(i,j):
    if(i>=j):
        return(0)
    
    minans = sys.maxsize
    for k in range(i,j):
        temp_ans = solve(i,k) + solve(k+1,j) + (arr[i-1]*arr[k]*arr[j])
        minans = min(minans,temp_ans)
    return(minans)

print(solve(1,len(arr)-1))