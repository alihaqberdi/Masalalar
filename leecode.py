# 1108
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# 1920
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]


# 2011
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if "--" in i:
                x -= 1
                continue
            x+=1
        return x


# 1422
class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1,len(s)):
            left = s[:i]
            right = s[i:]
            num = left.count('0') + right.count("1")
            if num > ans:
                ans = num
        return ans


# 2
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans, num, vl1, vl2 = [], 0, 1, 1
        while True:
            val1, val2 = 0, 0
            if vl1:
                val1 = l1.val
            if vl2:
                val2 = l2.val
            data, mod = divmod(val1 + val2 + num, 10)
            ans.append(mod)
            num = data
            if not l1.next:
                vl1 = 0
            else:
                l1 = l1.next
            if not l2.next:
                vl2 = 0
            else:
                l2 = l2.next
            if not (vl2 or vl1):
                if num:
                    ans.append(num)
                break
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        data = ListNode(ans.pop(-1))
        for i in ans[::-1]:
            data = ListNode(i, data)
        return data


# 1446
class Solution:
    def maxPower(self, s: str) -> int:
        res, num, current = 1, 1, s[0]
        for i in s[1:]:
            if i == current:
                num += 1
            else:
                num = 1
            if res < num:
                res = num
            current = i   
        return res


# 2274
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:     
        special.sort()
        if special[-1]<top:
            special.append(top+1)
        max_ = 0
        old = bottom
        for i in special:
            if i - old > max_:
                max_ = i - old
            old = i+1
        return max_


# 6
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        data = {}
        counter = 1
        minus = 0
        def change_data(key, val):
            if data.get(key):
                data[key] = data[key] + val
                return
            data[key] = val
        for i in s:
            if counter == 1:
                minus = 0
                change_data(1, i)
            elif counter == numRows:
                minus = 1
                change_data(numRows, i)
            else:
                change_data(counter, i)
            if minus:
                counter -= 1
            else:
                counter += 1
        return "".join(data.values())


# 28
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        one = len(haystack)
        two = len(needle)
        if one < two:
            return -1
        start = 0
        index_data = haystack[start:two]
        for i in range(one - two + 1):
            if index_data == needle:
                return start
            else:
                if one > two:
                    if one > two + 1:
                        two += 1
                        start += 1
                        index_data = haystack[start:two]
                    else:
                        two+=1
                        start += 1
                        index_data = haystack[start:]
                else:
                    return -1


# 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_set = set()
        max_length = 0
        left, right = 0, 0
        while right < len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                right += 1
                max_length = max(max_length, right - left)
            else:
                char_set.remove(s[left])
                left += 1
        return max_length


        
