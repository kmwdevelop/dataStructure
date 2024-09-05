class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
      
    def isEmpty(self) :
        if self.top == -1 :
            print("Stack is empty")
            return True
        else :
            return False
        
    def isFull(self):
        if self.top == self.capacity - 1 :
            print("Stack is full")
            return True