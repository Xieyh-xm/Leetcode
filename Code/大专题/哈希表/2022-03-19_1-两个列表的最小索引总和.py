'''
两个列表的最小索引总和
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
'''

from ast import List
import sys


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1, dict2 = {}, {}
        for i, val in enumerate(list1):
            dict1[val] = i
        '''这一步可以优化，不需要两个hashmap'''
        for i, val in enumerate(list2):
            dict2[val] = i
        min_sum=sys.maxsize
        restaurant=[]
        for key in dict1:
            if key in dict2:
                cur_sum=dict1[key]+dict2[key]
                if cur_sum<min_sum:
                    min_sum=cur_sum
                    restaurant=[key]
                elif cur_sum==min_sum:
                    restaurant.append(key)
        return restaurant