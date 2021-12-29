class arrayadt:

    arr = [-1 for i in range(1000)]
    n=-1

    def __init__(self):
       self.n = int( input("Enter array size") )
       for i in range(self.n):
           self.arr[i] = int(input())

    def get(self,pos):
        return(self.arr[pos])
    
    def set(self,pos,num):
        self.arr[pos] = num
    
    def insert(self,pos,num):
        for i in range(self.n-1,pos-1,-1):
            self.arr[i+1] = self.arr[i]
        self.arr[pos] = num
        self.n += 1
    
    def delete(self,pos):
        for i in range(pos,self.n-1):
            self.arr[i] = self.arr[i+1]
        self.n -= 1
    
    def display(self):
        for i in range(self.n):
            print(self.arr[i],end="\t")
        print()

    def linear_srch(self,num):
        fl = -1
        for i in range(self.n):
            if( self.arr[i] == num):
                fl = i
                break
        return(fl)
    
    def binary_srch(self,num):
        lo = 0
        hi = self.n-1
        fl = -1
        while(lo<=hi):
            mid = (lo+hi)//2
            if(self.arr[mid]==num):
                fl = mid
                break
            elif( self.arr[mid]>num ):
                hi = mid-1
            elif( self.arr[mid]<num ):
                lo = mid+1
        return(fl)
            





arr = arrayadt()
print(arr.get(1))
#arr.set(2,7)
arr.display()
#arr.insert(2,89)
arr.display()
arr.delete(3) 
arr.display()   
print(arr.linear_srch(1))
print(arr.binary_srch(1))
arr.display()