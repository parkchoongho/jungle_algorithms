class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        val_dict = {}
        
        for i in range(len(nums)):
            target_num = target - nums[i]
            if nums[i] in val_dict:
                return [val_dict[nums[i]], i]
            else: 
                val_dict[target_num] = i