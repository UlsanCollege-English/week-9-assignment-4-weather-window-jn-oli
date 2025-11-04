from collections import deque

def sliding_window_max(nums, k):
    # Handle edge cases
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]

    dq = deque()   # stores indices, not values
    result = []

    for i, num in enumerate(nums):
        # Remove indices that are out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller values from the back
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Record max for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
