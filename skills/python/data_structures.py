"""
Data Structures - Skills for GitHub Copilot CLI
This file demonstrates working with various data structures in Python.
"""


class Stack:
    """Simple stack implementation using a list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item from stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in stack."""
        return len(self.items)


class Queue:
    """Simple queue implementation using a list."""
    
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add item to back of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item from queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        # Note: pop(0) has O(n) time complexity. For O(1) dequeue,
        # use collections.deque with popleft() in production code.
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items in queue."""
        return len(self.items)


class Node:
    """Node for linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Simple singly linked list implementation."""
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        """Add item to end of list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """Add item to beginning of list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    # Test Stack
    print("Testing Stack:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack size: {stack.size()}")
    print(f"Pop: {stack.pop()}")
    print(f"Peek: {stack.peek()}")
    
    # Test Queue
    print("\nTesting Queue:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue size: {queue.size()}")
    print(f"Dequeue: {queue.dequeue()}")
    print(f"Front: {queue.front()}")
    
    # Test LinkedList
    print("\nTesting LinkedList:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    print(f"List: {ll.to_list()}")
    ll.delete(2)
    print(f"After delete: {ll.to_list()}")
