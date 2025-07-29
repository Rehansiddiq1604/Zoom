class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, new_data):
        new_node = Node(new_data)
        if not new_node:
            print("\nStack Overflow")
            return
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("\nStack Underflow")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("\nStack is empty")
            return float('-inf')

st = Stack()
st.push(11)
st.push(22)
st.push(33)
st.push(44)
print("Top element is", st.peek())
print("Removing two elements...")
st.pop()
st.pop()
print("Top element is", st.peek())