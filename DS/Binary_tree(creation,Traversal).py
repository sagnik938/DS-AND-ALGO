class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

arr = []

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

def preorder(root):
    if(root == None):
        return

    arr.append(root.data)
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if(root == None):
        return

    inorder(root.left)
    arr.append(root.data)
    inorder(root.right)

def postorder(root):
    if(root == None):
        return

    postorder(root.left)
    postorder(root.right)
    arr.append(root.data)

root = CreateTree()  
preorder(root)
print(arr)
inorder(root)
print(arr)
postorder(root)
print(arr)



