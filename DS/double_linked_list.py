class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
    
    def get_data(self):
        return(self.data)
    
    def set_left(self,address):
        self.left = address
    
    def set_right(self,address):
        self.right = address
    
    def get_left(self):
        return(self.left)
    
    def get_right(self):
        return(self.right)

class Double_link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.prev = None
        self.count = 0

    def append_node(self,val):
        self.count += 1
        temp = Node(val)
        if( self.count == 1):
            self.head = self.tail = self.current = temp
        else:
            self.current.set_right(temp)
            temp.set_left(self.current)
            self.current = temp
            self.tail = self.current
        

    def traverse_front(self):
        front_trav = self.head
        while(front_trav != None):
            print(front_trav.get_data(),end = "\t-->\t")
            front_trav = front_trav.get_right()
        print("NULL")
    
    def traverse_back(self):
        back_trav = self.tail
        while(back_trav != None):
            print(back_trav.get_data(),end = "\t-->\t")
            back_trav = back_trav.get_left()
        print("NULL")

    def insert_begin(self,val):
        temp = Node(val)
        temp.set_right(self.head)
        self.head.set_left(temp)
        self.head = temp
    
    def insert_end(self,val):
        temp = Node(val)
        self.tail.set_right(temp)
        temp.set_left(self.tail)
        self.tail = temp
    
    def insert(self,pos,val):
        if(pos == 1):
            self.insert_begin(val)
        elif(pos == self.count):
            self.insert_end(val)
        else:
             head = self.head
             while(pos-1>1):
                head = head.get_right()
                pos-=1
             temp = Node(val)
             temp.set_left( head )
             temp.set_right(head.get_right())
             (head.get_right()).set_left(temp)
             head.set_right(temp)
       
    def delete_node(self,pos):
        head = self.head
        if(pos == 1):
            (self.head.get_right()).set_left(None)
            self.head = self.head.get_right()
        
        elif(pos == self.count):
            (self.tail.get_left()).set_right(None)
            self.tail = self.tail.get_left()
        
        else:
            while(pos-1>1):
                head = head.get_right()
                pos-=1
            ((head.get_right()).get_right()).set_left(head)
            head.set_right( (head.get_right()).get_right() )
        


    
DLL = Double_link_list()
for i in range(10):
    DLL.append_node(i+1)
DLL.insert(1,34)
DLL.traverse_front()
DLL.traverse_back()
DLL.delete_node(5)
DLL.delete_node(7)
DLL.traverse_front()
DLL.traverse_back()




