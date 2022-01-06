import sys

def pref_sum(arr):
    mx = arr[0]
    for i in range(1,len(arr)):
        arr[i] = arr[i-1] + arr[i]
        mx = max(mx,arr[i])
    return(mx)

def find(arr,queries):
    for q in queries:
        a = q[0]
        b = q[1]
        k = q[2]

        arr[a-1] += k
        if b < len(arr):
            arr[b] -= k 
    return(pref_sum(arr))

n = list(map(int,input().split()))
arr = [ 0 for i in range(n[0])]
queries = [ list(map(int,input().split())) for i in range(n[1]) ]
print(find(arr,queries))