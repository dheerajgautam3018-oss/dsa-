
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, key):
        return key % self.size

    # Insert
    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return

        self.table[index].append([key, value])

    # Get/Search
    def get(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return "Not Found"

    # Delete
    def delete(self, key):
        index = self.hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return "Deleted"

        return "Key Not Found"

    # Display
    def display(self):
        print(self.table)


# Main
h = HashTable(5)

h.insert(10, "A")
h.insert(15, "B")   # collision with 10
h.insert(20, "C")   # collision with 10 and 15

h.display()

print("Get 15:", h.get(15))

print(h.delete(15))
h.display()