class Solution(object):
    def __init__(self):
        self.lengthOfLastWord = self.lengthOfLastWord_01

    # Your runtime beats 68.57% of pythonsubmissions.
    def lengthOfLastWord_01(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])

    # Your runtime beats 44.30% of pythonsubmissions.
    def lengthOfLastWord_02(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for c in reversed(s):
            if c == ' ':
                if length == 0:
                    continue
                break
            length += 1
        return length


def sentence_gen(num_word):
    import random
    import string
    sentence = []
    for i in range(num_word):
        sentence.append(''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 10))]))
    return ' '.join(sentence)


def sets_gen(lengthOfLastWord):
    import random
    test_sets = []
    paragraph = '\n'.join([sentence_gen(random.randint(10, 15)) for _ in range(1000)])
    for s in paragraph.split('\n')[1:-1]:
        match = lengthOfLastWord(s)
        test_sets.append((s, match))
    return test_sets


def test(lengthOfLastWord, test_sets, msg):
    for s, match in test_sets:
        try:
            assert(lengthOfLastWord(s) == match)
        except AssertionError as ex:
            print(s, match, lengthOfLastWord(s))
            print(msg, '--> Assertion Error <--')


def test_spd(lengthOfLastWord, test_sets):
    for s, _ in test_sets:
        lengthOfLastWord(s)

if __name__ == '__main__':
    sol = Solution()
    # prep
    print('prep...')
    test_sets = sets_gen(sol.lengthOfLastWord)
    # test
    print('test...')
    test(sol.lengthOfLastWord_01, test_sets, '01')
    test(sol.lengthOfLastWord_02, test_sets, '02')
    # test_spd
    print('test_spd...')
    _stmt_ = 'test_spd(sol.lengthOfLastWord_{0:02d}, test_sets)'
    _setup_ = 'from __main__ import sol, test_sets, test_spd'
    _number_ = 1000
    import timeit
    print(timeit.timeit(stmt=_stmt_.format(01), setup=_setup_, number=_number_))
    print(timeit.timeit(stmt=_stmt_.format(02), setup=_setup_, number=_number_))


