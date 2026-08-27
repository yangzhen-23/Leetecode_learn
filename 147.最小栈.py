"""
请你设计一个 最小栈 。它提供 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data_stack=[]
        self.min_stack=[]
        

    def push(self, x: int) -> None:
        self.data_stack.append(x)
        if self.min_stack:
            top = self.min_stack[-1]
            min_value = min(top, x)
            self.min_stack.append(min_value)
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()