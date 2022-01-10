class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def CreateTree():
    temp = Node()
    val = input("Enter Value of Node, N for no node")
    
    if(val == "N"):
        return(None)
    
    temp.data = val
    print("Enter left of ",val)
    temp.left = CreateTree()
    print("Enter right of ",val)
    temp.right = CreateTree()

    return(temp)

def preorder(root,arr):
    if(root == None):
        return

    arr.append(root.data)
    preorder(root.left,arr)
    preorder(root.right,arr)

def inorder(root,arr):
    if(root == None):
        return

    inorder(root.left,arr)
    arr.append( root.data )
    inorder(root.right,arr)

def postorder(root,arr):
    if(root == None):
        return

    postorder(root.left,arr)
    postorder(root.right,arr)
    arr.append(root.data)

def traversal(root):
    opt = 0
    arr = []
    while(opt != 4):
        opt = int(input("Enter\n<1> for inorder\n<2> for post order\n<3> for preorder\n<4> to exit\n"))
        if( opt == 1):
           arr = [] 
           inorder(root,arr)
           print( arr ) 
        if( opt == 2):
           arr = []
           postorder(root,arr) 
           print( arr )
        if( opt == 3):
           arr = []
           preorder(root,arr) 
           print( arr )





root = CreateTree()  
traversal(root)






