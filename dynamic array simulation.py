class DynamicArray:
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.arr = [0] * self.capacity

    def append(self, val):
        # Check if resize needed before inserting
        if self.size == self.capacity:
            print("Resizing from", self.capacity, "to", self.capacity * 2)
            self.resize()

        self.arr[self.size] = val
        self.size += 1
        print(f"Inserted {val}, Size={self.size}, Capacity={self.capacity}")

    def resize(self):
        self.capacity *= 2
        new_arr = [0] * self.capacity

        # copy old elements to new array
        for i in range(self.size):
            new_arr[i] = self.arr[i]

        self.arr = new_arr
#testing the dynamic array implementation
da = DynamicArray()

da.append(10)
da.append(20)
da.append(30)
da.append(40)
da.append(50)