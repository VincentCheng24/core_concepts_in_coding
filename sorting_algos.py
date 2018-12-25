import numpy as np


class Solution():
    "sorting algos"

    def selection_sort_iterative(self, A):
        for i in range(len(A)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(A)):
                if A[min_idx] > A[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            A[i], A[min_idx] = A[min_idx], A[i]
        return A

    def selection_sort_rec(self, a, low, high):
        if low < high:
            temp_a = np.array(a[low:high+1])
            min_idx = np.where(temp_a == temp_a.min())[0][0] # to find the idx where the minimum locates
            a[low], a[min_idx+low] = a[min_idx+low], a[low]

            self.selection_sort_rec(a, low+1, high)
        return a

    def bubble_sort(self, a):
        n = len(a)
        orderred = True
        for i in range(n):

            for j in range(n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    orderred = False

            if orderred:
                return a

        return a

    def insertion_sort(self, a):
        n = len(a)

        for i in range(1, n):
            cur_idx = i
            cur_val = a[i]
            while a[cur_idx-1] > cur_val and cur_idx >0:
                a[cur_idx] = a[cur_idx-1]
                cur_idx -= 1
            a[cur_idx] = cur_val

        return a

    def merge(self, a, l, m, r):
        nl = m - l + 1
        nr = r - m

        L = [0] * nl
        R = [0] * nr

        for i in range(nl):
            L[i] = a[l+i]

        for i in range(nr):
            R[i] = a[m+i+1]

        i = 0
        j = 0
        k = l

        while i < nl and j < nr:
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        while i < nl:
            a[k] = L[i]
            i += 1
            k += 1

        while j < nr:
            a[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, a, l, r):
        if l < r:
            m = (l+r) // 2
            self.merge_sort(a, l, m)
            self.merge_sort(a, m+1, r)
            self.merge(a, l, m, r)
        return a

    def partition_high(self, a, low, high):
        pivot_idx = low -1
        pivot = a[high]

        for i in range(low, high):
            if a[i] < pivot:
                pivot_idx += 1
                a[i], a[pivot_idx] = a[pivot_idx], a[i]
        a[pivot_idx+1], a[high] = a[high], a[pivot_idx+1]

        return pivot_idx+1

    def partition_low(self, a, low, high):
        pivot_idx = high + 1
        pivot = a[low]

        for i in range(low, high):
            if a[high-i] > pivot:
                pivot_idx -= 1
                a[high-i], a[pivot_idx] = a[pivot_idx], a[high-i]
        a[pivot_idx-1], a[low] = a[low], a[pivot_idx-1]

        return pivot_idx-1

    def quick_sort_recursive(self, a, low, high):
        if low < high:
            pivot_idx = self.partition_low(a, low, high)

            self.quick_sort_recursive(a, low, pivot_idx-1)
            self.quick_sort_recursive(a, pivot_idx+1, high)
        return a

    def quick_sort_iterative(self, a, low, high):

        size = len(a)
        stack = [0] * size
        top = -1

        top += 1
        stack[top] = low
        top += 1
        stack[top] = high

        while top >= 0:
            high = stack[top]
            top -= 1
            low = stack[top]
            top -= 1

            p_idx = self.partition_high(a, low, high)

            if p_idx + 1 < high:
                top += 1
                stack[top] = p_idx + 1
                top += 1
                stack[top] = high

            if p_idx - 1 > low:
                top += 1
                stack[top] = low
                top += 1
                stack[top] = p_idx - 1

        return a

    def heapify(self, a, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        max_idx = i

        if l < n and a[max_idx] < a[l]:
            max_idx = l

        if r < n and a[max_idx] < a[r]:
            max_idx = r

        if max_idx != i:
            a[max_idx], a[i] = a[i], a[max_idx]
            self.heapify(a, n, max_idx)

        return a

    def heap_sort(self, a):
        n = len(a)

        for i in range(n-1, -1, -1):
            self.heapify(a, n, i)

        for i in range(n-1, 0, -1):
            a[i], a[0] = a[0], a[i]
            self.heapify(a, i, 0)

        return a

    def shell_sort(self, a):

        stride = len(a) // 2

        while stride > 0:
            for i in range(stride, len(a)):
                cur_idx = i
                cur_val = a[i]
                while a[cur_idx - stride] > cur_val and cur_idx >= stride: # it requires the = as idx 0 has ele
                      a[cur_idx] = a[cur_idx - stride]
                      cur_idx -= stride
                a[cur_idx] = cur_val

            stride = stride // 2

        return a

    def counting_sort(self, a):
        n = len(a)
        cnt_len = max(a) + 1
        cnt = [0] * cnt_len
        res = [0] * n

        # counting the appearance
        for i in a:
            cnt[i] += 1

        cnt[0] -= 1 # to decrement each element for zero-based indexing
        for i in range(1, cnt_len):
            cnt[i] = cnt[i] + cnt[i-1]

        # it becomes necessary to reverse the list
        # when this function needs to be a stable sort
        for i in reversed(a):
            res[cnt[i]] = i
            cnt[i] -= 1
        return res

    def counting_sort_ranged(self, a):
        n = len(a)
        cnt_len = max(a) - min(a) + 1
        s = min(a)
        cnt = [0] * cnt_len
        res = [0] * n

        # counting the appearance
        for i in a:
            cnt[i-s] += 1

        cnt[0] -= 1 # to decrement each element for zero-based indexing
        for i in range(1, cnt_len):
            cnt[i] = cnt[i] + cnt[i-1]

        # it becomes necessary to reverse the list
        # when this function needs to be a stable sort
        for i in reversed(a):
            res[cnt[i-s]] = i
            cnt[i-s] -= 1
        return res

    def bucket_sort(self, a):
        mx = max(a)
        mn = min(a)

        # if mx > 1000, apply multiple times, starting from the smallest digit

        if mn < 0 or mx > 100:
            return 'only numbers range(100)'
        else:
            buckets = dict()
            res = []
            for i in range(10):
                buckets[i] = []
            for ele in a:
                buckets[ele//10].append(ele)

            for key, lis in buckets.items():
                self.insertion_sort(lis)

            for key, lis in buckets.items():
                res += lis

            return res

    def counting_sort_for_radix_sort(self, a, base):

        n = len(a)
        res = [0] * n
        cnt = [0] * 10

        for i in a:
            idx = i // base % 10
            cnt[idx] += 1

        cnt[0] -= 1
        for i in range(1, 10):
            cnt[i] += cnt[i-1]

        for ele in reversed(a):
            idx = ele // base % 10
            res[cnt[idx]] = ele
            cnt[idx] -= 1

        return res

    def radix_sort(self, a):
        mx = max(a)
        base = 1
        while mx//base > 0:
            a = self.counting_sort_for_radix_sort(a, base)
            base *= 10
        return a




a = [64, 34, 25, 12, 22, 11, 90]
b = [3, 5, 6]
solver = Solution()
print('original a:', a)
# print('bubble sort:', solver.bubble_sort(a))
# print('insertion_sort:', solver.insertion_sort(a))
# print('merge_sort:', solver.merge_sort(a, 0, len(a)-1))
# print('quick_sort:', solver.quick_sort_iterative(a, 0, len(a)-1))
# print('selection_sort_rec:', solver.selection_sort_rec(a, 0, len(a)-1))
print('heap_sort:', solver.heap_sort(a))
# print('shell_sort:', solver.shell_sort(a))
# print('counting_sort:', solver.counting_sort_ranged(a))
# print('bucket_sort:', solver.bucket_sort(a))
print('radix_sort:', solver.radix_sort(a))
