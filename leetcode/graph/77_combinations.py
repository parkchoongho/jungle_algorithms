class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        result = []

        def dfs(nums, start, k):
            if k == 0:
                result.append(nums[:])
                return

            for i in range(start, n + 1):
                nums.append(i)
                dfs(nums, i + 1, k - 1)
                nums.pop()

        dfs([], 1, k)
        return result



