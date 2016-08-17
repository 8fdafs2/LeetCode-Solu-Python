'''
Created on May 9, 2016

@author: ray.wang
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        if isinstance(x, int):
            self.val = x
            self.next = None
        elif type(x) is list:
            self.val = x[0]
            self.next = None
            l = self
            for val in x[1:]:
                l.next = ListNode(val)
                l = l.next
        else:
            raise Exception("Constuctor Argument Error")
        
    def vals(self):
        l = self
        ret = [l.val,]
        while l.next:
            l = l.next
            ret.append(l.val)
        return ret
    
    

class Solution(object):
    
    def __init__(self):
        self.addTwoNumbers = self.addTwoNumbers_01    
    
    # Approach #01 (Recur SubFunc)
    # 20160509 : Your runtime beats 45.71% of pythonsubmissions.
    def addTwoNumbers_01(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def f(l1, l2, carry):
        
            if l1 and l2:
            
                val = l1.val + l2.val + carry
                
                if val >= 10:
                    lr = ListNode(val - 10)
                    lr.next = f(l1.next, l2.next, 1)
                else:
                    lr = ListNode(val)
                    lr.next = f(l1.next, l2.next, 0)
                
                return lr
            
            elif l1:
            
                val = l1.val + carry
                
                if val >= 10:
                    lr = ListNode(val - 10)
                    lr.next = f(l1.next, None, 1)
                else:
                    lr = ListNode(val)
                    lr.next = f(l1.next, None, 0)
                
                return lr
            
            elif l2:
            
                val = l2.val + carry
            
                if val >= 10:
                    lr = ListNode(val - 10)
                    lr.next = f(None, l2.next, 1)
                else:
                    lr = ListNode(val)
                    lr.next = f(None, l2.next, 0)
                
                return lr
            
            elif carry:
                
                return ListNode(carry)
            
            return None
        
        return f(l1, l2, 0)
    
    # Approach #02 (While)
    # 20160509 : Your runtime beats 73.93% of pythonsubmissions.
    def addTwoNumbers_02(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        _lr_ = lr = ListNode(0)
        carry = 0
        
        while True:
        
            if l1 and l2:
            
                val = l1.val + l2.val + carry
            
                if val >= 10:
                    carry = 1
                    lr.next = ListNode(val - 10)
                else:
                    carry = 0
                    lr.next = ListNode(val)
                
                lr = lr.next
                l1 = l1.next
                l2 = l2.next
            
            elif l1:
            
                val = l1.val + carry
            
                if val >= 10:
                    carry = 1
                    lr.next = ListNode(val - 10)
                else:
                    carry = 0
                    lr.next = ListNode(val)
                    
                lr = lr.next
                l1 = l1.next
                l2 = None
            
            elif l2:
            
                val = l2.val + carry
                
                if val >= 10:
                    carry = 1
                    lr.next = ListNode(val - 10)
                else:
                    carry = 0
                    lr.next = ListNode(val)
                    
                lr = lr.next
                l1 = None
                l2 = l2.next
            
            elif carry:
                
                lr.next = ListNode(carry)
                lr = lr.next
                l1 = None
                l2 = None
                
                break
            
            else:
                
                break
            
        return _lr_.next
    
    
def test(addTwoNumbers = None, test_sets = None):
    for l1, l2, match in test_sets:
        assert(addTwoNumbers(l1, l2).vals() == match)


def test_spd(addTwoNumbers = None, test_sets = None):
    for l1, l2, _ in test_sets:
        addTwoNumbers(l1, l2)


def sets_get(addTwoNumbers = None):
    import random
    test_sets = []
    for i in range(1, 10):
        for j in range(1, 10):
            l1 = ListNode([random.randint(0, 10) for _ in range(i)])
            l2 = ListNode([random.randint(0, 10) for _ in range(j)])
            match = addTwoNumbers(l1, l2).vals()
            test_sets.append((l1, l2, match))
    return test_sets
  
if __name__ == '__main__':

    # prep
    print('prep...')
    sol = Solution()
    test_sets = sets_get(sol.addTwoNumbers)
    
    # test
    print('test...')
    test(sol.addTwoNumbers_01, test_sets)
    test(sol.addTwoNumbers_02, test_sets)

    # test_spd
    print('test_spd...')
    _stmt_ = "test_spd(sol.addTwoNumbers_{:02d}, test_sets)"
    _setup_ = "from __main__ import sol, test_spd, test_sets"
    _number_ = 1000

    import timeit
    print(timeit.timeit(stmt=_stmt_.format(1), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(2), setup=_setup_, number=_number_))