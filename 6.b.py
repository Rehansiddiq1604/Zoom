class Queue:
    def __init__(self):
        self.queue=[]
    def is_empty(self):
        return len(self.queue)==0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
def is_palindrome(s):
    queue=Queue()
    for char in s:
        queue.enqueue(char)
    while queue.size()>1:
        if queue.dequeue()!=queue.queue[-1]:
            return False
        queue.queue.pop()
    return True
test="radar"
if is_palindrome(test):
    print(f'"{test}" is a palindrome.')
else:
    print(f'"{test}" is not a palindrome.')
test="hello"
if is_palindrome(test):
    print(f'"{test}" is a palindrome.')
else:
    print(f'"{test}" is not a palindrome.')
