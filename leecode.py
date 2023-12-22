
# 1108
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# 1920
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]
