
class Search():
    '''
    a collection of searching algos for self-study
    '''

    def linearSearch(self, a, key):

        for i in range(len(a)):
            if a[i] == key:
                return i
        return -1

    def binearSearch(self, a, key):
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












a = [ 2, 100, 3, 4, -10, 10, 40 ]
b = []
x = -10

solver = Search()
print('linearSearch:', solver.linearSearch(a, x))
print('binearSearch:', solver.binearSearch(a, x))
print('linearSearch:', solver.linearSearch(a, x))
print('linearSearch:', solver.linearSearch(a, x))