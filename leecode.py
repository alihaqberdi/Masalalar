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

        
