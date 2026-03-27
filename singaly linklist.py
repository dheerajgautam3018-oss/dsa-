class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # Inserting at beginning
    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    #  Deleted by value 
    def delete(self, key):
        temp = self.head

        #  delete head node if it matches the key
        if temp and temp.data == key:
            self.head = temp.next
            print(f"{key} deleted (was head)")
            return

        prev = None

        # Search for key to be deleted, keep track of previous node
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        #  element not found in the list
        if temp is None:
            print(f"{key} not found")
            return

        # delete middle/last node by changing next of previous node
        prev.next = temp.next
        print(f"{key} deleted")

    # Traversing the list and printing the elements
    def traverse(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")


#  Testing the singly linked list implementation
sll = SLL()

sll.insert(10)
sll.insert(20)
sll.insert(30)

print("List after insertion:")
sll.traverse()

sll.delete(20)

print("List after deletion:")
sll.traverse()