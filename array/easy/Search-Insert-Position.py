class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            print(nums.index(target))
        else:
            nums.append(target)
            nums.sort()
        return (nums.index(target))