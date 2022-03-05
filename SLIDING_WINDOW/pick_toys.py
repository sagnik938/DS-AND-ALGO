def solve(arr,n,k):
    i = j = 0
    lookup = {}
    mx = -9999
    while( j < n ):
        if( arr[j] in list(lookup.keys())):
            lookup.update({arr[j] : lookup[arr[j]]+1 })
        else:
            lookup.update({arr[j]:1})
        
        if( len(lookup) < k):
            j += 1
        elif( len(lookup) == k ):
            mx = max(mx,j-i+1)
            j += 1
        elif( len(lookup) > k ):
            while( len(lookup) > k ):
                if( lookup[arr[i]] == 1):
                    del lookup[arr[i]]
                else:
                    lookup.update({arr[i] : lookup[arr[i]]-1})
                i += 1
            j += 1
    return(mx)

arr = "abaccab"
print(solve(arr,len(arr),2))
            
