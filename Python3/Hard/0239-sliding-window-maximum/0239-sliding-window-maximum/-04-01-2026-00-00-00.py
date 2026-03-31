from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        n = len(nums)
        l = 0

        for r in range(n):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            if r >= k-1:
                res.append(q[0])
                if nums[l] == q[0]:
                    q.popleft()
                l += 1
        
        return res