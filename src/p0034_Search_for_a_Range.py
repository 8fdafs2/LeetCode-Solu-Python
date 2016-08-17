class Solution(object):

    def __init__(self):
        self.searchRange = self.searchRange_01
        
    # Binary Search then One-by-One Upper/Lower Bound Search
    # 20160511 : Your runtime beats 25.68% of pythonsubmissions.
    def searchRange_01(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rrange = [-1, -1]
        
        if not nums: return rrange
        
        lo = 0
        hi = len(nums)
                
        while lo < hi:
            mid = (lo + hi) // 2
            midvar = nums[mid]
            if midvar < target:
                lo = mid + 1
            elif midvar > target:
                hi = mid
            else:
                rrange = [mid, mid]
                for i in range(lo, mid):
                    if nums[i] == target:
                        rrange[0] = i
                        break
                for i in range(hi - 1, mid, -1):
                    if nums[i] == target:
                        rrange[1] = i
                        break
                break
                
        return rrange
        
        
    # Binary Search then Binary Upper/Lower Bound Search 
    # 20160511 : Your runtime beats 25.68% of pythonsubmissions.
    def searchRange_02(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rrange = [-1, -1]
        
        if not nums: return rrange
        
        lo = 0
        hi = len(nums)
        
        # Search in Range: (lo, hi)
        while lo < hi:
            mid = (lo + hi) // 2
            midvar = nums[mid]
            if midvar < target:
                lo = mid + 1
            elif target < midvar:
                hi = mid
            else:
                rrange = [mid, mid]
                
                _hi_ = hi
                _mid_ = mid
                
                # Search in Range: (lo, mid-1)
                hi = _mid_
                while lo < hi:
                    mid = (lo + hi) // 2
                    if nums[mid] < target:
                        lo = mid + 1
                    else: # midvar == target
                        rrange[0] = hi = mid
                
                # Search in Range: (mid+1, hi-1)
                lo = _mid_ + 1
                hi = _hi_
                while lo < hi:
                    mid = (lo + hi) // 2
                    if target < nums[mid]:
                        hi = mid
                    else: # midvar == target
                        lo = mid + 1
                        rrange[1] = mid
                        
                break
                
        return rrange
        
    # Binary Lower Bound Search then Binary Upper Bound Search 
    # 20160511 : Your runtime beats 16.30% of pythonsubmissions.
    def searchRange_03(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rrange = [-1, -1]
        
        if not nums: return rrange
        
        # lower Bound Search
        
        lo = 0
        hi = length = len(nums)
                
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else: # target <= midvar
                hi = mid
                
        if lo < length and nums[lo] == target:
            rrange[0] = lo
        else:
            return rrange
        
        hi = length
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else: # midvar < target
                hi = mid
                
        rrange[1] = lo - 1
        
        return rrange
        
def test(searchRange = None, test_sets = None):
    for nums, target, match in test_sets:
        assert(searchRange(nums, target) == match)
        
def test_spd(searchRange = None, test_sets = None):
    for nums, target, _ in test_sets:
        searchRange(nums, target)
            
def sets_get(searchRange = None):
    import random
    test_sets = []
    for i in range(100):
        nums = sorted([random.randint(0, 10) for _ in range(i)])
        target = random.randint(0, 10)
        match = searchRange(nums, target)
        test_sets.append((nums, target, match))
    return test_sets

if __name__ == '__main__':

    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.searchRange)

    # test
    print('test...')
    test(sol.searchRange_01, test_sets)
    test(sol.searchRange_02, test_sets)
    test(sol.searchRange_03, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = "test_spd(sol.searchRange_{:02d}, test_sets)"
    _setup_ = "from __main__ import sol, test_spd, test_sets"
    _number_ = 2000

    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(3), setup=_setup_, number=_number_))