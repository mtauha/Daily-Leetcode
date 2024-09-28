class MyCircularDeque:
    """
        Design your implementation of the circular double-ended queue (deque).

        Implement the MyCircularDeque class:
        
        MyCircularDeque(int k) Initializes the deque with a maximum size of k.
        boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
        boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
        boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
        boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
        int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
        int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
        boolean isEmpty() Returns true if the deque is empty, or false otherwise.
        boolean isFull() Returns true if the deque is full, or false otherwise.
    """

    def __init__(self, k):
        self.queue = [0] * k
        self.front = 0
        self.rear = k - 1
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
