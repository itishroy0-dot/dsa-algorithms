class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()   # [10, 20, 30]
print(s.pop())  # 30
s.display()   # [10, 20]
