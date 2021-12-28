class weightedObjs:

    w=0
    p=0
    r=0.0

    def __init__(self, w , p):
        self.w = w
        self.p = p
        self.r = p/w


def partition(start,end,objs):
    pivIndex = start
    piv = objs[start].r
    
    while( start < end):
        while( start<len(objs) and objs[start].r<=piv):
              start+=1
        while( objs[end].r > piv ):
              end-=1
        if(start<end):
              objs[start] , objs[end] = objs[end] , objs[start]
    
    objs[end] , objs[pivIndex] = objs[pivIndex] , objs[end]
    return(end)


def quicksort(start,end,objs):
    if(start<end):
        p = partition(start,end,objs)
        quicksort(start,p-1,objs)
        quicksort(p+1,end,objs)

def fractional_knapsack(objs,n,W):
    quicksort(0,n-1,objs)
    prof = 0
    pos = n
    for i in range(n-1,-1,-1):
        if( objs[i].w <= W and W > 0 ):
            prof += objs[i].p
            W -= objs[i].w
            pos = i
    if( W > 0):
        pos-=1
        prof += objs[pos].r * W
        W=0

    return(prof)


wt = list(map(int,input("Enter Weights ").split()))
profit = list(map(int,input("Enter Profits ").split()))
W = int(input("Enter knapsack capacity"))

if(len(wt) != len(profit)):
    print("Invalid Input")
else:
    n = len(wt)
    objs=[]
    for i in range(n):
        objs.append( weightedObjs(wt[i],profit[i]) )
    print(fractional_knapsack(objs,n,W))


