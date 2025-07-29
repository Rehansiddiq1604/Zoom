class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    # Function to check if the queue is empty
    def isEmpty(self):
        return self.front is None

    # Function to add an element to the queue
    def enqueue(self, new_data):
        new_node = Node(new_data)
        if self.isEmpty():
            self.front = self.rear = new_node
            self.printQueue()
            return
        self.rear.next = new_node
        self.rear = new_node
        self.printQueue()

    # Function to remove an element from the queue
    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        self.printQueue()

    # Function to print the current state of the queue
    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        queue_string = "Current Queue: "
        while temp is not None:
            queue_string += str(temp.data) + " "
            temp = temp.next
        print(queue_string)

q = Queue()

# Enqueue elements into the queue
q.enqueue(10)
q.enqueue(20)

# Dequeue elements from the queue
q.dequeue()
q.dequeue()

# Enqueue more elements into the queue
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# Dequeue an element from the queue
q.dequeue()