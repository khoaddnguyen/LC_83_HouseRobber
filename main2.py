# House Robber II - houses are arranged in a circle
def rob(self, nums: List[int]) -> int:

    # skipping first and last house
    # nums[0] added in case array only has 1 house
    return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))


def helper(self, nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n+1,...]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

