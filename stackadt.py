class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Underflow"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


# some test cases 
s = Stack()
s.push(10)
s.push(20)
print(s.pop())   # output is 20
print(s.peek())  #output is 10