class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:
    def __init__(self):
        self.root = None
        self.length = 0
    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            while curr.left != node or curr.right != node:
                print(curr)
                if value < curr.val:
                    if curr.left == None:
                        curr.left = node
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = node
                        break
                    else:
                        curr = curr.right
        self.length += 1
    def lookup(self, value):
        if self.root == None:
            raise IndexError
        else:
            curr = self.root
            while curr != None:
                if curr.val == value:
                    return True
                if value > curr.val:
                    curr = curr.right
                else:
                    curr = curr.left
            return False
    def remove(self, value):
        if self.root == None:
            raise IndexError
        else:
            parentNode = None
            currNode = self.root
            while currNode.val != value:
                if value > currNode.val:
                    parentNode = currNode
                    currNode = currNode.right
                else:
                    parentNode = currNode
                    currNode = currNode.left
            if currNode.right == None:
                if currNode.left.val > parentNode.val:
                    parentNode.right = currNode.left
                else:
                    parentNode.left = currNode.left
            elif currNode.right.left == None:
                if currNode.right.val > parentNode.val:
                    currNode.right.left = currNode.left
                    parentNode.right = currNode.right
                else:
                    currNode.right.left = currNode.left
                    parentNode.left = currNode.right
            else:
                leaf = currNode.right
                while leaf.left != None:
                    leaf = leaf.left
                leaf.left = currNode.left
                leaf.right = currNode.right
                if leaf.val > parentNode.val:
                    parentNode.right = leaf
                else:
                    parentNode.left = leaf

def main():
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    print(bst.lookup(15))
    bst.remove(15)
    print(bst.lookup(15))

if __name__ == "__main__":
    main()
                
