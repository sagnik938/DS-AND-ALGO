import sys

arr="nitik"

mat = [[-1 for i in range(1000)]for j in range(1000)]

def isPalindrome(s):
    return s == s[::-1]

def solve(i,j):
    if(i>=j or isPalindrome( arr[i:j+1] )):
        return(0)

    if(mat[i][j] != -1):
        return( mat[i][j] )
    
    minans = sys.maxsize
    for k in range(i,j):

      if( mat[i][k] != -1 ):
          left = ( mat[i][k] )
      else:
          left = solve(i,k)

      if( mat[k+1][j] != -1):
          right = mat[k+1][j]
      else:
          right = solve(k+1,j)

      minans = min(minans,left + right + 1)
      mat[i][j]= minans


    return(mat[i][j])

def disp( n ):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end="\t")
        print()

print(solve(0,len(arr)-1))
disp(len(arr))