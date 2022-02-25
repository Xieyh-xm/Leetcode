'''
验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
---------------------------------------------
输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
---------------------------------------------
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''左右指针'''
        left_index, right_index = 0, len(s) - 1
        while right_index > left_index:
            while (s[left_index] < '0' or s[left_index] > '9') and (s[left_index] < 'A' or s[left_index] > 'Z') and (
                    s[left_index] < 'a' or s[left_index] > 'z'):
                left_index += 1
                if left_index > len(s) - 1:
                    break
            while (s[right_index] < '0' or s[right_index] > '9') and (
                    s[right_index] < 'A' or s[right_index] > 'Z') and (s[right_index] < 'a' or s[right_index] > 'z'):
                right_index -= 1
                if right_index < 0:
                    break
            if right_index <= left_index:
                break

            left_s = (ord(s[left_index]) - ord('a')) % (ord('a') - ord('A'))
            right_s = (ord(s[right_index]) - ord('a')) % (ord('a') - ord('A'))
            # 还得考虑数字
            if (left_s == right_s and s[left_index] >= 'A' and s[right_index] >= 'A') or (
                    s[left_index] == s[right_index]):
                left_index += 1
                right_index -= 1
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(str(solution.isPalindrome("0P")))
