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


# 13
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        pre = 0
        res = 0
        for i in s:
            v = val[i]
            if pre < v:
                res -= pre*2
            res += v
            pre = v
        return res


# 9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


# 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


# 1496
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        data = {
            (0, 0): 1
        }
        curr = (0, 0)
        for j, i in enumerate(path, start=1):
            if i == "N":
                run = (curr[0] + 1, curr[-1])
            elif i == "S":
                run = (curr[0] - 1, curr[-1])
            elif i == 'W':
                run = (curr[0], curr[-1] - 1)
            else:
                run = (curr[0], curr[-1] + 1)
            if data.get(run):
                return True
            data[run] = 1
            curr = run
        return False


# 1662
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)


# 1758
class Solution:
    def minOperations(self, s: str) -> int:
        def min_count(s, start):
            ans = 0
            cur = start
            for i in s:
                if i == cur:
                    ans += 1
                cur = "0" if cur == "1" else "1"
            return ans
        return min((min_count(s, "0"), min_count(s, "1")))


# 151
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        for i in s.split()[::-1]:
            if i != " ":
                res += (i+" ")
        return res[:-1]


# 1768
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        len_w1 = w1
        len_w2 = w2
        res = []
        while len_w2 or len_w1:
            if len_w1:
                res.append(word1[w1 - len_w1])
                len_w1 -= 1
            if len_w2:
                res.append(word2[w2 - len_w2])
                len_w2 -= 1
        return "".join(res)    


# 1929
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2    


# 2469
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


# 771
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in jewels:
            if i in stones:
                res += stones.count(i)
        return res


# 2942
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for i, e in enumerate(words):
            if x in e:
                res.append(i)
        return res


# 1672
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])


# 2798
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i in hours:
            if i >= target:
                res += 1
        return res


# 2894
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if i % m:
                num1 += i
                continue
            num2 += i
        return num1 -num2 


# 2413
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2


# 2235
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


# 1678
class Solution:
    def interpret(self, command: str) -> str:
        res = []
        inde = 0
        for i in command:
            if i == "G":
                res.append("G")
            elif i == "(" and command[inde+1] == ")":
                res.append("o")
            elif i == "(" and command[inde+1] == "a":
                res.append('al')
            inde += 1
        return "".join(res)


# 1480
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        sum_ = 0
        for i in nums:
            sum_ += i
            res.append(sum_)
        return res
