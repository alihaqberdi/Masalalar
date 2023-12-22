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
        
