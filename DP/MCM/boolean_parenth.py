def incrementor(lt, lf, rt, rf, k, param):
    if( param ):
        if( k == "|" ):
           return ((lt*rf)+(lf*rt)+(lt*rt))
        elif( k == "&" ):
            return ((lt*rt))
        elif( k == "^" ):
            return ((lt*rf)+(lf*rt))
    
    else:
         if( k == "|" ):
           return ((lf*rf))
         elif( k == "&" ):
            return ((lt*rf)+(lf*rt)+(lf*rf))
         elif( k == "^" ):
            return ((lt*rt)+(lf*rf))

def solve( exp , start , stop , param):

    #base condition
    if( start > stop):
       return( 0 )
    if( start==stop ):
        if( param ):
            return( 1 if exp[start]=="T" else 0)
        else:
            return( 1 if exp[start]=="F" else 0)
    
    cnt = 0
    #recursion
    for k in range(start+1,stop,2):
        lt = int(solve(exp,start,k-1,True)) 
        lf = int(solve(exp,start,k-1,False)) 
        rt = int(solve(exp,k+1,stop,True)) 
        rf = int(solve(exp,k+1,stop,False)) 
        cnt+=( incrementor( lt, lf, rt, rf, exp[k], param))
    return(cnt)

exp = "T|T&F^T"
param = 0

print(solve(exp,0,len(exp)-1,param))
#print(incrementor(4,2,2,4,"^",True))

    
