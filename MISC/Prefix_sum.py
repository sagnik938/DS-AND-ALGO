def pref_sum(arr):
    for i in range(1,len(arr)):
        arr[i] = arr[i-1] + arr[i]

def answer(queries,arr):
    if(queries[0] == 0):
        return( arr[q[1]] )
    else:
        return( arr[q[1]] - arr[q[0]-1])

arr = [1,2,3,4,5,6,7,8,9]
queries = [ [0,3] , [1,2] , [3,4] , [0,4] , [1,6] , [2,6] , [3,7] ]
pref_sum(arr)
for q in queries:
    print(answer(q,arr))