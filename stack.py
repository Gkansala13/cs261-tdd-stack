# Stack: A stack.
# Your implementation should pass the tests in stack.py.
# Grayson Kansala

class Stack:

    def __init__(self):
        self.stack=[]

    def is_empty(self):
        return len(self.stack)==0
            
    def pop(self):
        if self.is_empty():
            raise IndexError('Index is empty')
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError('Index is empty')
        else:
            return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
    
