size = 10
bloom = [0] * size


# Hash Functions
def hash1(item):
    return sum(ord(c) for c in item) % size


def hash2(item):
    return (sum(ord(c) * 2 for c in item)) % size


# Insert item
def add(item):
    bloom[hash1(item)] = 1
    bloom[hash2(item)] = 1


# Check membership
def check(item):
    if bloom[hash1(item)] == 1 and bloom[hash2(item)] == 1:
        return "Possibly Present"
    else:
        return "Definitely Not Present"


# Main
add("apple")
add("banana")

print("Bloom Filter:", bloom)

print("apple:", check("apple"))
print("banana:", check("banana"))
print("mango:", check("mango"))