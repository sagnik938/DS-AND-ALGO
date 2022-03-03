def first_negative(arr,n,k):
    i = j = 0
    negs = []
    answer = []
    while(j<n):
        if(arr[j]<0):
            negs.append(arr[j])
        if( j-i+1 < k):
            j += 1
        else:
            print(negs)
            if(len(negs)==0):
                answer.append(0)
                i += 1
                j += 1
            else:
                  answer.append(negs[0])
                  if( negs[0] == arr[i]):
                    negs.pop(0)
                  i += 1
                  j += 1
    return(answer)

arr = [12,-1,-7,8,-15,30,16,28]
n = len(arr)
k = 2
print(first_negative(arr,n,k))