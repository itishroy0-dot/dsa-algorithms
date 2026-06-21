class DynamicArray:
    def __init__(self):
        self.array = []

    def insert(self, value):
        self.array.append(value)

    def delete(self, index):
        if 0 <= index < len(self.array):
            self.array.pop(index)

    def display(self):
        print(self.array)


# Example usage
da = DynamicArray()
da.insert(10)
da.insert(20)
da.insert(30)
da.display()   # [10, 20, 30]
da.delete(1)
da.display()   # [10, 30]
