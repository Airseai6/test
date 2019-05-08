#! -*- coding:utf-8 -*-
# Leetcode 刷题记录


# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         3. 无重复字符的最长子串
#         :type s: str
#         :rtype: int
#         """
#         self.s = s
#         strpool = ''
#         n_max, n_tem = 0, 0
#         for i in range(len(self.s)):
#             if self.s[i] in strpool:
#                 find = strpool.index(s[i])
#                 strpool = strpool[find+1:] + s[i]
#                 n_tem = len(strpool)
#             else:
#                 strpool = strpool + self.s[i]
#                 print(strpool)
#                 n_tem +=1
#                 if n_tem > n_max:
#                     n_max = n_tem
#
#         return n_max
#
#
# if __name__ == '__main__':
#     s = Solution()
#     str1 = "abcabcbb"
#     m = s.lengthOfLongestSubstring(str1)
#     print(m)


# def myAtoi(str1):
#     """
#     第8题字符串转整数
#     :type str: str
#     :rtype: int
#     """
#     if str1 is '' or str1.isspace():
#         return 0
#     str2 = str1.split()[0]
#     num_s = ''
#     for item in str2:
#         if (item == '+' or item == '-') and len(num_s) == 0:
#             num_s += item
#         else:
#             try:
#                 n = int(item)
#                 num_s += str(n)
#             except:
#                 break
#     try:
#         num = int(''.join(num_s))
#         if num < -(2**31):
#             return -(2**31)
#         elif num > 2**31-1:
#             return 2**31-1
#         else:
#             return num
#     except:
#         return 0
#
#
# if __name__ == '__main__':
#     s = "-5ooo"
#     print(myAtoi(s))


def maxArea(height):
    """
    11题，成水最多容器
    :type height: List[int]
    :rtype: int
    """
    def fun_l(height, start, end, result=0):
        if start < end:
            if result == 0:
                result = min(height[start], height[end]) * (end - start)
            i, j = start, end
            left_temp, right_temp = height[i], height[j]
            while i < j:
                while (i < j) and (height[i] <= left_temp):
                    i += 1
                temp = min(height[i], height[j]) * (j - i)
                if temp > result:
                    result = temp
                while (i < j) and (height[j] <= right_temp):
                    j -= 1
                temp = min(height[i], height[j]) * (j - i)
                if temp > result:
                    result = temp
            fun_l(height, start, i-1, result)
            fun_l(height, j+1, end, result)
        return result

    # return fun_l(height, 0, len(height)-1, result=0)
    # def fun_r(height, start, end, result=0):
    #     if start < end:
    #         if result == 0:
    #             result = min(height[start], height[end]) * (end - start)
    #         i, j = start, end
    #         right = height[j]
    #         while i < j and height[i] <= right:
    #             j -= 1
    #         temp = min(height[i], height[j]) * (j - i)
    #         if temp > result:
    #             result = temp
    #         fun_r(height, start, j, result)
    #     return result

    result = 0
    for i in range(len(height)-1):
        tem = fun_l(height, i, len(height)-1)
        if tem > result:
            result = tem
        tem = fun_l(height, 0, len(height)-1-i)
        if tem > result:
            result = tem
    return result


if __name__ == '__main__':
    height = [2,3,4,5,18,17,6]
    print(maxArea(height))


# def romanToInt(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     d = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#     l = len(s)
#     num = d[s[0]]
#     for i in range(1,l):
#         if d[s[i]] > d[s[i-1]]:
#             num += d[s[i]] - 2*d[s[i-1]]
#         else:
#             num += d[s[i]]
#     return num



# def intToRoman(num):
#     """
#     12题
#     :type num: int
#     :rtype: str
#     """
#     d = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
#     ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
#     ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
#     ['', 'M', 'MM', 'MMM']]
#     out = []
#     out.append(d[3][int(num/1000)])
#     out.append(d[2][int(num / 100%10)])
#     out.append(d[1][int(num % 100 / 10)])
#     out.append(d[0][int(num % 10)])
#     outs = ''.join(out)
#     return outs
#
#
# if __name__ == '__main__':
#     print(intToRoman(1994))


# def longestCommonPrefix(strs):
#     """
#     14题
#     :type strs: List[str]
#     :rtype: str
#     """
#     if strs == []:
#         return ''
#     elif len(strs) == 1:
#         return strs[0]
#     else:
#         short = len(min(strs,key=len))
#     m = 0
#     for n in range(short):
#         break_flag = False
#         for i in range(1, len(strs)):
#             if strs[i][n] != strs[0][n]:
#                 break_flag = True
#                 break
#         if break_flag:
#             break
#         m += 1
#     if m == 0:
#         s_out = ''
#     else:
#         s_out = strs[0][:m]
#     return s_out
#
#
# if __name__ == '__main__':
#     strs = ["dog","racecar","car"]
#     print(longestCommonPrefix(strs))


# def threeSum(nums):
#     """
#     15题
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#     注意：答案中不可以包含重复的三元组。
#     例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#     满足要求的三元组集合为：
#     [
#       [-1, 0, 1],
#       [-1, -1, 2]
#     ]
#     """
#     d = []
#     if nums.count(0) > 2:
#         d.append([0,0,0])
#     l = len(nums)
#     for k1 in range(l-2):
#         for k2 in range(k1+1,l-1):
#             for k3 in range(k2+1,l):
#                 if nums[k1] + nums[k2] + nums[k3] == 0:
#                     tu = [nums[k1], nums[k2], nums[k3]]
#                     f = len(d)
#                     if f == 0:
#                         d.append(tu)
#                     else:
#                         flag = True
#                         for t in range(f):
#                             if nums[k1] in d[t-1] and nums[k2] in d[t-1] and nums[k3] in d[t-1]:
#                                 flag = False
#                         if flag:
#                             d.append(tu)
#     print(d)
#
#
# if __name__ == '__main__':
#     nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#     threeSum(nums)


# def letterCombinations(digits):
#     """
#     17题电话号码字母的自由组合
#     :type digits: str
#     :rtype: List[str]
#     """
#     d ={
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz"
#     }
#     pool = []
#     di = []
#     for item_n in digits:
#         for item_s in d[item_n]:
#             di.append(item_s)


# def removeDuplicates(nums):
#     """
#     26. 删除排序数组中的重复项
#     :type nums: List[int]
#     :rtype: int
#     """
#     new = []
#     for item in nums:
#         if item not in new:
#             new.append(item)
#     length = len(new)
#     nums[:length] = new
#     return length


# def removeElement(nums, val):
#     """
#     27移除元素
#     :type nums: List[int]
#     :type val: int
#     :rtype: int
#     """
#     while val in nums:
#         nums.remove(val)
#     return len(nums)


# def strStr(haystack, needle):
#     """
#     28,字符串
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     if needle is '':
#         return 0
#     if needle in haystack:
#         return haystack.index(needle)
#     else:
#         return -1
#
#
# if __name__ == '__main__':
#     print(strStr("mississippi", 'issip'))


# def findSubstring(s, words):
#     """
#     30. 与所有单词相关联的字串
#     :type s: str
#     :type words: List[str]
#     :rtype: List[int]
#     """
#     import copy
#     def perm(listVar):
#         if len(listVar) == 1:
#             return [listVar]
#         retlist = []
#         for i in range(len(listVar)):
#             # 得到一个新的列表，列表中去掉了i指向的元素
#             restList = listVar[:i] + listVar[i + 1:]
#             # 1
#             # perm([2,3])-> [[2,3],[3,2]]
#             # 1 加到 perm(2,3) 的结果中去
#             perResult = perm(restList)
#             for x in perResult:
#                 retlist.append(listVar[i:i + 1] + x)
#         return retlist
#
#     res = []
#     l_list = [x for x in range(len(words))]
#     for item in perm(l_list):
#         item_s = ''
#         for i in item:
#             item_s = item_s + words[i]
#         item_s_c = s.count(item_s)
#         if item_s_c == 1:
#             res.append(s.index(item_s))
#         elif item_s_c > 1:
#             s_t = copy.deepcopy(s)
#             while item_s_c >= 1:
#                 i_t = s_t.index(item_s)
#                 res.append(i_t)
#                 s_t = s_t[:i_t] + '*' +s_t[i_t+1:]
#                 item_s_c = s_t.count(item_s)
#     res = list(set(res))
#     return res
#
#
# if __name__ == '__main__':
#     s = "aaa"
#     words = ["a", "a"]
#     print(findSubstring(s, words))
#     print(s.count('aa'))


