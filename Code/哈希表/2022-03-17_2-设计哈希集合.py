'''
设计哈希集合
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 MyHashSet 类：
·void add (key）向哈希集合中插入值 key。
·bool contains (key）返回哈希集合中是否存在这个值 key。
·void remove (key）将给定值 key 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。
'''


class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.set.append(key)

    def remove(self, key: int) -> None:
        for i, val in enumerate(self.set):
            if val == key:
                if i + 1 < len(self.set):
                    self.set = self.set[:i] + self.set[i + 1:]
                else:
                    self.set = self.set[:i]

    def contains(self, key: int) -> bool:
        for val in self.set:
            if val == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
