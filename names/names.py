import time
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        if not self:
            self = BSTNode(value)
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
    def contains(self, target):
        if self.value is None:
            return False
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
        else:
            return True

def sortedArrayToBST(arr):
    if not arr:
        return None
    mid = (int(len(arr) / 2))
    root = BSTNode(arr[mid])
    
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid+1:])
    return root
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = sorted(f.read().split("\n"))  # List containing 10000 names
f.close()

bst = sortedArrayToBST(names_1)

f = open('names_2.txt', 'r')
names_2 = sorted(f.read().split("\n"))  # List containing 10000 names
f.close()

# #STRETCH
# set1 = set(names_1)
# set2 = set(names_2)
# duplicates = set1.intersection(set(names_2))  # Return the list of duplicates in this data structure

duplicates = []
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)


end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
