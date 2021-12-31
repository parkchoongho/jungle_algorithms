from collections import deque


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])
                return
            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)

                prev_elements.append(element)
                dfs(next_elements)
                prev_elements.remove(element)

        dfs(nums)

        return result