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

class Queue:
    def __init__(self):
        self.top = None
        self.rear = None
        self.temp = None
        self.current = None
    
    def enqueue(self,val):
        self.temp = Node(val)
        if( self.current == None):
            self.top = self.rear = self.current = self.temp
        else:
            self.current.set_address(self.temp)
            self.rear = self.temp
            self.current = self.temp
    
    def dequeue(self):
        if(self.top==None):
            return("Queue Underflow")
        else:
            k = self.top.getdata()
            self.top = self.top.get_address()
            return(k)
    
    def peek(self):
        if(self.top==None):
            return("Empty")
        else:
            return(self.top.getdata())

q = Queue()
for i in range(10):
    q.enqueue(i*2)

for i in range(6):
    print(q.dequeue())
print(q.peek())