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

def height(node):
    if node is None:
        return -1 ; 

    else :

        # Compute the depth of each subtree
        lDepth = height(node.left)
        rDepth = height(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
        
def dolvlOrder(root,level,arr):
    if( root == None):
        return(0)
    if( level == 1):
        arr.append(root.data)
    else:
        dolvlOrder(root.left,level-1,arr)
        dolvlOrder(root.right,level-1,arr)
     
            
def levelOrder(root,arr):
    #Write your code here
    ht = height(root)
    i = 1
    while(i<=ht+1):
        dolvlOrder(root,i,arr)
        i += 1

def operations(root):
    opt = 0
    arr = []
    while(opt != 6):
        opt = int(input("Enter\n<1> for inorder\n<2> for post order\n<3> for preorder\n<4> to print height\n<5> to do level order traversal\n<6> to exit"))
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
        if(opt == 4):
            print(height(root))
        if(opt == 5):
            arr = []
            levelOrder(root,arr) 
            print( arr )


root = CreateTree()  
operations(root)




