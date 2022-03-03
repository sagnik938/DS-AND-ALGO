from threading import local
from turtle import back


def find_max(arr,n,k):
    i = j = 0

    localmax =[]
    back = -1

    answer = []
    while( j < n ):
        while( len(localmax) > 0 and localmax[back]<arr[j]):
            localmax.pop(back)
            back -= 1
        localmax.append(arr[j])
        back += 1

        if(j-i+1<k):
            j += 1
        else:
            answer.append(localmax[0])
            if( arr[i] == localmax[0]):
                localmax.pop(0)
                back -= 1
            i += 1
            j += 1

    return(answer)





arr = [1,3,-1,-3,5,3,6,7]
n = len(arr)
k = 6
print(find_max(arr,n,k))