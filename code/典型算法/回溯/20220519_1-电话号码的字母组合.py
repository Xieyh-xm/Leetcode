'''电话号码的字母组合'''
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2': 'abc', '3': 'def',
                '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ret, path = [], []

        def backtracking(startIdx) -> None:
            if len(path) == len(digits):
                str = "".join(path)
                if str != "":
                    ret.append("".join(path))
                return
            for i in range(len(dict[digits[startIdx]])):
                letter = dict[digits[startIdx]]
                path.append(letter[i])
                backtracking(startIdx + 1)
                path.pop()
            return

        backtracking(0)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))
