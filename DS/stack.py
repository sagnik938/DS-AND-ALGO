class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

    def set_address(self,address):
        self.next = address
    
    def get_address(self):
        return(self.next)
    
    def getdata(self):
        return(self.data)

class stack:
    def __init__(self):
        self.top = None
        self.current = None
        self.temp = None

    def push(self,val):
        self.temp = Node(val)
        (self.temp).set_address( (self.current) )
        self.current = self.temp
        self.top = self.temp
    
    def pop(self):
        if(self.top == None):
            return("Stack Underflow")
        k = self.top.getdata()
        self.top = self.top.get_address()
        return(k)
    
    def peek(self):
        if(self.top == None):
            print("Stack Underflow")
        print( self.top.getdata())
    
stck = stack()
for i in range(10):
    stck.push(i*2)

print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
print(stck.pop())
stck.peek()
stck.peek()
