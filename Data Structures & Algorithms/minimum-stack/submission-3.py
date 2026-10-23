class MinStack:
    #class attributes
    def __init__(self):
        self.list = []
        self.min_in_stack = []
    
    def push(self, val: int) -> None:
        self.list.append(val)
        if not self.min_in_stack or val <= self.min_in_stack[-1]:
            self.min_in_stack.append(val)


        #check if last elemet(smallest curr in stack) > cur val --> new val becomes the smallest so we append to the min_in_stack stack
        if self.min_in_stack[-1] > val:
            self.min_in_stack.append(val)
        
    def pop(self) -> None:
        #just slices the last
        value = self.list.pop()
        #checks if the popped value is the min --> if so we gotta remove and alteranate to the next min value that is stil within the stack
        if value == self.min_in_stack[-1]:
            self.min_in_stack.pop()



    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min_in_stack[-1]
        
