#  Node class for queue implementation using singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#  Queue using Singly Linked List
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    #  Enqueue  added at rear
    def enqueue(self, x):
        new = Node(x)
        if self.rear is None:
            self.front = self.rear = new
            print(f"Enqueued: {x}")
            return

        self.rear.next = new
        self.rear = new
        print(f"Enqueued: {x}")

    #  Dequeue (it is removed from front)
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(f"Dequeued: {temp.data}")
        return temp.data

    #  Get front element without remooving it
    def get_front(self):
        if self.front is None:
            return None
        return self.front.data

    #  Display queue elements
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


#  Testing the queue implementation
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Queue:")
q.display()

q.dequeue()

print("After dequeue:")
q.display()

print("Front element:", q.get_front())