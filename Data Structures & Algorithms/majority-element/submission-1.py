class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = Counter(nums)
        for k, v in majorityElement.items():
            maxi = max(majorityElement, key=lambda k: majorityElement[k])
            return maxi