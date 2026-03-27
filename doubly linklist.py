class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # Insert at beginning of the list
    def insert_begin(self, data):
        new = DNode(data)
        if self.head:
            self.head.prev = new
            new.next = self.head
        self.head = new

    #  Insert after a given node (identified by value)
    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("Previous node cannot be NULL")
            return

        new = DNode(data)
        new.next = prev_node.next
        prev_node.next = new
        new.prev = prev_node

        if new.next:
            new.next.prev = new

        print(f"{data} inserted after {prev_node.data}")

    #  Delete node at position (pos is 0-based index)
    def delete_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        # Move to position to be deleted
        for _ in range(pos):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        # If deleting head node
        if temp.prev is None:
            self.head = temp.next
            if self.head:
                self.head.prev = None
        else:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print(f"Node at position {pos} deleted")

    #  Traverse forward and print the list elements
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("NULL")