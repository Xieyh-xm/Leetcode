'''
常数时间插入、删除和获取随机元素

实现 RandomizedSet 类：

·RandomizedSet（）初始化 RandomizedSet 对象
·bool insert (int val）当元素 va1 不存在时，向集合中插入该项，并返回 true；否则，返回 false。
·bool remove (int val）当元素 val 存在时，从集合中移除该项，并返回 true；否则，返回 false。
·int getRandom（）随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。

每个元素应该有相同的概率被返回。
你必须实现类的所有函数，并满足每个函数的平均时间复杂度为O(1)。
'''


from os import remove
from random import random
from re import T


class RandomizedSet:

    def __init__(self):
        self.num_idx_dict = dict()
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val in self.num_idx_dict:
            return False
        else:
            self.num_list.append(val)
            self.num_idx_dict[val] = len(self.num_list)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.num_idx_dict:
            return False
        else:
            # # 把最后一个移动到remove的位置
            # remove_idx = self.num_idx_dict[val]
            # del self.num_idx_dict[val]
            # if len(self.num_list)>1:
            # # 修改最后一个元素的idx
            #     self.num_idx_dict[self.num_list[-1]] = remove_idx # 如果要删除的值是最后一个，会有问题
            #     self.num_list[remove_idx] = self.num_list[-1]
            # self.num_list.pop()
            # return True
            # 把最后一个移动到remove的位置
            remove_idx = self.num_idx_dict[val]
            # 修改最后一个元素的idx
            self.num_idx_dict[self.num_list[-1]] = remove_idx
            self.num_list[remove_idx] = self.num_list[-1]
            del self.num_idx_dict[val]
            self.num_list.pop()
            return True

    def getRandom(self) -> int:
        seed = random.randint(0, len(self.num_list)-1)
        return self.num_list[seed]

        # Your RandomizedSet object will be instantiated and called as such:
        # obj = RandomizedSet()
        # param_1 = obj.insert(val)
        # param_2 = obj.remove(val)
        # param_3 = obj.getRandom()
