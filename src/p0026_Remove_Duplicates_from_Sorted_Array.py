'''
Created on May 9, 2016

@author: ray.wang
'''
class Solution(object):
    
    def __init__(self):
        self.removeDuplicates = self.removeDuplicates_01
    
    # Approach #01 (list.remove)
    # 20160509 : Your runtime beats 2.31% of pythonsubmissions.
    def removeDuplicates_01(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        
        num_dict = {}
        
        i = 0
        
        while i < len(nums):
            
            num = nums[i]
            
            if num not in num_dict:
                num_dict[num] = None
                i += 1
            else:
                nums.remove(num)
                
    # Approach #02 ()
    # 20160509 : Your runtime beats 16.63% of pythonsubmissions.
    def removeDuplicates_02(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return

        num_dict = {}
        
        for num in nums:
            
            if num not in num_dict:
                num_dict[num] = 0
            else:
                num_dict[num] += 1
                
        i = 0
        
        for num in sorted(num_dict.keys()):
#         for num in sorted(set(nums)):
            
            if num_dict[num] > 0:
            
                del nums[i + 1: i + 1 + num_dict[num]]
#                 nums[i:-num_dict[num]] = nums[i + num_dict[num]:-num_dict[num]]
            
            i += 1
            
            
                
def test(removeDuplicates = None, test_sets = None):
    for nums, length, match in test_sets:
        if match:
            assert(removeDuplicates(nums)[:length] == match)
        else:
            assert(removeDuplicates(nums) == None)
            
def test_spd(removeDuplicates = None, test_sets = None):
    for nums, _, _ in test_sets:
        removeDuplicates(nums)
    
def sets_get(removeDuplicates = None):
    import random
    test_sets = []
    for i in range(100):
        nums = sorted([random.randint(0, 10) for _ in range(i)])
        length = len(set(nums))
        match = removeDuplicates(nums)
        if match:
            test_sets.append((nums, length, match[:length]))
        else:
            test_sets.append((nums, 0, None))
    return test_sets

if __name__ == '__main__':

    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.removeDuplicates)

    # test
    print('test...')
    test(sol.removeDuplicates_01, test_sets)
    test(sol.removeDuplicates_02, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = "test_spd(sol.removeDuplicates_{:02d}, test_sets)"
    _setup_ = "from __main__ import sol, test_spd, test_sets"
    _number_ = 1000

    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))             

