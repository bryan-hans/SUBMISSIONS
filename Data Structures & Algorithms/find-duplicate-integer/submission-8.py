class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        curr = head 

        while curr:
            val = curr.val
            if val in seen:
                return val
            else:
                seen.add(val)
        