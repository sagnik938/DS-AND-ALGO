def solve(arr,n):
    lookup = {}
    i = j = 0
    mx = -999
    while(j<n):
        if( arr[j] in list(lookup.keys())):
            lookup.update({arr[j]:lookup[arr[j]]+1})
        else:
            lookup.update({arr[j]:1})
        
        if( len(lookup.keys()) == j-i+1 ):
            mx = max(mx,j-i+1)
            j += 1
        elif( len(lookup.keys()) < j-i+1 ):
            while( len(lookup.keys()) < j-i+1 ):
                  if( lookup[arr[i]] == 1):
                    del lookup[arr[i]]
                  else:
                    lookup.update({arr[i]:lookup[arr[i]]-1})
                  i += 1
            j +=1
        print(lookup,mx)
    return(mx)

arr = "pwwkews"
print(solve(arr,len(arr)))