def solve( x , y):
    if( len(x) != len(y) ):
        return(False)
    if(len(x) < 1):
        return(False)
    if( x == y):
        return(True)
    
    flag = False
    n = len(x)
    for i in range(1,n):
        cond1 = ( solve( x[n-i:n] , y[0:i] ) and solve( x[0:n-i] , y[i:n] ) )
        cond2 = ( solve( x[0:i] , y[0:i] ) and solve( x[i:n] , y[i:n] ) )
        if( cond1 or cond2 ):
            flag = True
            break
    return(flag)

s1 = input()
s2 = input()
print(solve(s1,s2))