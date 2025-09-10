class Node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def _init_(self):
        self.root=None
    def insert(self,data):
        new_node=Node(data)
        if self.root is None:
            self.root=new_node
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            if current.left is None:
                current.left=new_node
                return
            else:
                queue.append(current.left)
                if current.right is None:
                    current.right=new_node
                    return
                else:
                    queue.append(current.right)
    def print(self):
        if self.root is None:
            return
        queue=[self.root]
        while queue:
            current=queue.pop(0)
            print(current.data,end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
tree=BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(60)
print("Level order traversal:")
tree.print()
