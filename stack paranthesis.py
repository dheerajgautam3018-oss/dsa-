#  Node class for stack implementation using linklist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


#  Stack using Singly Linked List implementation
class StackLL:
    def __init__(self):
        self.head = None

    def push(self, x):
        new = Node(x)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            print("Underflow")
            return None
        val = self.head.data
        self.head = self.head.next
        return val


# Balanced Parentheses Checker using stack
def is_balanced(expr):
    s = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for ch in expr:
        if ch in "({[":
            s.append(ch)
        elif ch in ")}]":
            if not s or s.pop() != pairs[ch]:
                return False
    return len(s) == 0


# Testing the stack implementation and balanced parantheses checker
print(is_balanced("{()}"))   # output: True
print(is_balanced("{(})"))   # output: False