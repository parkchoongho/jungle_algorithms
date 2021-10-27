class Solution(object):
    def twoSum(self, nums: list, target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        1. 첫번째 수를 뺀 결과 키 조회
        """
        # val_dict = {}

        # for i in range(len(nums)):
        #     target_num = target - nums[i]
        #     if nums[i] in val_dict:
        #         return [val_dict[nums[i]], i]
        #     else:
        #         val_dict[target_num] = i

        """
        2. 포인터 2개 활용        
        """
        copy_nums = nums[:]
        copy_nums.sort()

        left = 0

        right = len(copy_nums) - 1

        while left < right:
            if (copy_nums[left] + copy_nums[right]) > target:
                right -= 1
            elif (copy_nums[left] + copy_nums[right]) < target:
                left += 1
            else:
                return [nums.index(copy_nums[left]), nums.index(copy_nums[right])]
