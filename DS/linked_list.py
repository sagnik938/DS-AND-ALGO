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
    
class LinkedList:
    def __init__(self):
        self.start = None
        self.current = None
        self.temp = None
        self.count = 0
    
    def append_node(self,val):
        self.count += 1
        self.temp = Node(val)

        if(self.count==1):
            self.start = self.current = self.temp
        else:
            (self.current).set_address(self.temp)
            self.current = self.temp
        self.temp.set_address(None)

    def view(self):
        head = self.start
        while(head != None):
            print( head.getdata(),end="\t")
            head = head.get_address()
        print()
    
    def sorted_insert_node(self,val):
        head = self.start
        fl = -1
        while(  head.get_address()!=None and (head.get_address()).getdata() < val ):
            head = head.get_address()
            fl = 0
        if(fl==-1):
            temp = Node(val)
            temp.set_address(head)
            self.start = temp
        else:
             temp = Node(val)
             temp.set_address( head.get_address() )
             head.set_address(temp)

    def insert_node(self,pos,val):
        head = self.start
        if(pos==1):
            temp = Node(val)
            temp.set_address(head)
            self.start = temp
        else:
            for i in range(1,pos-1):
                head = head.get_address()
            temp = Node(val)
            temp.set_address(head.get_address())
            head.set_address(temp)

    def delete_node(self,pos):
        head = self.start
        for i in range(1,pos-1):
            head = head.get_address()
        head.set_address( (head.get_address()).get_address() ) 


LL = LinkedList()
for i in range(10):
    LL.append_node(i*2)
LL.view()
LL.sorted_insert_node(-1)
LL.sorted_insert_node(-2)
LL.insert_node(5,69)
LL.view()
LL.delete_node(5)
LL.view()



