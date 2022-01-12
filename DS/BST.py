import random

class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def CreateBST(val,root):
    if( root == None ):
        temp = Node()
        temp.data = val
        return(temp)
    else:
        if( val > root.data):
            root.right = CreateBST(val,root.right)
        else:
            root.left = CreateBST(val,root.left)

    return(root)

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

def searchBST(val,root):
    if(root == None):
        return(None)
    if(root.data == val):
        return(root)
    if(val>root.data):
        return( searchBST(val,root.right) )
    if(val<root.data):
        return( searchBST(val,root.left) )

def LCA(v1,v2,root):
    if(root.data < v1 and root.data < v2 ):
        return(LCA(v1,v2,root.right))
    if(root.data > v1 and root.data > v2 ):
        return(LCA(v1,v2,root.left))
    return(root)

def deleteNode(root,val):
    if( root == None):
        return root
    
    if( val > root.data):
        root.right = deleteNode(root.right,val)
    elif( val < root.data):
        root.left = deleteNode(root.left,val)
    
    
    if root.left is None and root.right is None:
          return None

    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp


    succParent = root

    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.data = succ.data

    return root
    

def operations(root):
    opt = 0
    arr = []
    while(opt != -1):
        opt = int(input("Enter\n<1> for inorder\n<2> for post order\n<3> for preorder\n<4> to search\n<5> for level order\n<6> for height\n<7> for Lowest Common Ancestor\n<8> to delete\n<-1> to exit"))
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
        if( opt == 4):
            val = int(input("Enter search val:-\t"))
            val = searchBST(val,root)
            if(val == None):
                print("value not found")
            else:
                print(str(val.data) + " found at location:- " + str(val))
        if(opt == 5):
            arr = []
            levelOrder(root,arr) 
            print( arr )
        if(opt == 6):
            print(height(root))
        if(opt==7):
            vals = list(map(int,input().split()))
            ancestor = LCA(vals[0],vals[1],root)
            print(ancestor.data)
        if( opt == 8):
            num = int(input("Enter val to be deleted"))
            deleteNode(root,num)

root = None
items = []
for i in range(20):
    num = random.randint(0,100)
    root = CreateBST(num,root)
    items.append(num)

print(items)
operations(root)