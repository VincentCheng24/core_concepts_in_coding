
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

        while l <= h:
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













a = [ 2, 3, 4, 10, 40 ]
b = []
x = 10

solver = Search()
print('linearSearch:', solver.linearSearch(a, x))
print('binearSearchIter:', solver.binearSearchIter(a, x))
print('binarySearchRecs:', solver.binarySearchRecs(a, x, 0, len(a)-1))
print('linearSearch:', solver.linearSearch(a, x))