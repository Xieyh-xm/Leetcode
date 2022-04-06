'''
最小栈
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

实现 Minstack 类：
- Minstack() 初始化堆栈对象。
- void push (int val）将元素 val 推入堆栈。
- void pop() 删除堆栈顶部的元素。
- int top() 获取堆栈顶部的元素。
- int getMin() 获取堆栈中的最小元素。
'''


class MinStack:

    def __init__(self):
        self.nums = []
        self.index = -1

    def push(self, val: int) -> None:
        self.nums.append(val)
        if self.index == -1:
            self.index = 0
        elif self.nums[self.index] > val:
            self.index = len(self.nums) - 1

    def pop(self) -> None:
        if self.index == len(self.nums) - 1:
            # 循环一下找最小值
            self.index = 0
            for i in range(len(self.nums) - 1):
                if self.nums[self.index] > self.nums[i]: self.index = i
        self.nums = self.nums[:-1]

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.nums[self.index]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
