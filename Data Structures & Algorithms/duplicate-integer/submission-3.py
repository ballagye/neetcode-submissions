class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            hashset.add(n)
        if len(hashset) != len(nums):
            return True
        else:
            return False

                
              

        