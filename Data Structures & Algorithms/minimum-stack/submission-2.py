class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = None
        self.minim_stack_size = 0
        self.minim_stack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minim_stack_size == 0 or val <= self.minim:
            self.minim_stack.append(val)
            self.minim = val
            self.minim_stack_size += 1
        
    def pop(self) -> None:
        if self.stack[-1] == self.minim:
            self.minim_stack.pop()
            self.minim_stack_size -= 1
            if self.minim_stack_size > 0:
                self.minim = self.minim_stack[-1]
            else:
                self.minim = None
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minim
        
