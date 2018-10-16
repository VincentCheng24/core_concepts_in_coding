import math


class Search():
    '''
    a collection of searching algos for self-study
    '''

    def linearSearch(self, a, key):

        for i in range(len(a)):
            if a[i] == key:
                return i
        return -1

    def binearSearchIter(self, a, key):
        '''
        a must be a sorted list/array
        '''
        print(a)
        l = 0
        h = len(a)

        while l < h:
            m = (l + h) // 2
            if a[m] == key:
                return m
            elif a[m] < key:
                l = m + 1
            else:
                h = m - 1

        return -1

    def binarySearchRecs(self, a, key, low, high):

        if low <= high:
            m = (low + high) // 2

            if a[m] == key:
                return m
            elif a[m] < key:
                # it's crucial to have a return here, otherwise no value returned
                return self.binarySearchRecs(a, key, m+1, high)
            else:
                return self.binarySearchRecs(a, key, low, m-1)
        else:
            return -1

    def jumpSearch(self, a, key):
        s = int(math.sqrt(len(a)))

        cur_idx = 0
        while cur_idx < len(a)-1 and a[cur_idx] < key:
            cur_idx += s
            # cur_idx = min(cur_idx, len(a)-1)  # to make sure the high is checked if cur_idx > high

        if a[len(a)-1] < key or a[0] > key:
            return -1
        for i in range(cur_idx-s, min(cur_idx+1, len(a))): # be careful to the critical value
            if a[i] == key:
                return i

        else:
            return -1

    def interpolationSearch(self, a, key):
        h = len(a) - 1
        l = 0

        while l < h and a[l] < key and a[h] > key:
            pos = int(l + (key - a[l]) * (h - l) / (a[h] - a[l]))
            if a[pos] == key:
                return pos
            elif a[pos] < key:
                l = pos + 1
            else:
                h = pos - 1
        # else:
        return -1

    def exponentialSearch(self, a, key):

        i = 1

        if a[0] > key and a[-1] < key:
            return -1

        while i < len(a)-1  and a[i] < key:
            i *= 2

        high = min(i+1, len(a))
        return self.binearSearchIter(a[i//2: high], key) + i//2









a = [ 2, 3, 4, 5, 6, 7, 8, 10, 40 ]
arr = [10, 12, 13, 16, 18, 19, 20, 21, \
                22, 23, 24, 33, 35, 42, 47]
b = []
x = 6

solver = Search()
# print('linearSearch:', solver.linearSearch(a, x))
# print('binearSearchIter:', solver.binearSearchIter(a, x))
# print('binarySearchRecs:', solver.binarySearchRecs(a, x, 0, len(a)-1))
# print('jumpSearch:', solver.jumpSearch(a, x))
# print('interpolationSearch:', solver.interpolationSearch(arr, x))
print('exponentialSearch:', solver.exponentialSearch(a, x))
# print('jumpSearch:', solver.jumpSearch(a, x))
# print('jumpSearch:', solver.jumpSearch(a, x))