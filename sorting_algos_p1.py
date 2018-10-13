import numpy as np


class Solution():
    "sorting algos"

    def selection_sort_iterative(self, a):

        for i in range(0, len(a)):
            mn = a[i]
            mn_idx = i
            for j in range(i+1, len(a)):
                if mn > a[j]:
                    mn = a[j]
                    mn_idx = j
            a[i], a[mn_idx] = a[mn_idx], a[i]

        return a

    def selection_sort_rec(self, a, low, high):

        mn = a[low]
        mn_idx = low
        if low < high:
            for i in range(low+1, high+1):
                if mn > a[i]:
                    mn = a[i]
                    mn_idx = i
            a[mn_idx], a[low] = a[low], a[mn_idx]
            self.selection_sort_rec(a, low+1, high)

        return a

    def bubble_sort(self, a):

        ordered = True

        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                ordered = False

        if ordered:
            return a

        return a

    def insertion_sort(self, a):

        for i in range(1, len(a)):
            cur_val = a[i]
            cur_idx = i
            while cur_idx > 0 and cur_val < a[cur_idx-1]:
                a[cur_idx] = a[cur_idx-1]
                cur_idx -= 1
            a[cur_idx] = a[i]

        return a

    def merge(self, a, l, m, r):
        nl = m - l + 1
        nr = r - m

        L = [0] * nl
        R = [0] * nr

        for i in range(nl):
            L[i] = a[i+l]

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
        p_val = a[high]
        p_idx = low-1

        for i in range(low, high):
            if a[i] < p_val:
                p_idx += 1
                a[p_idx], a[i] = a[i], a[p_idx]

        a[p_idx+1], a[high] = a[high], a[p_idx+1]

        return p_idx + 1

    def partition_low(self, a, low, high):
        p_val = a[low]
        p_idx = high + 1

        for i in range(high, low, -1):
            if a[i] > p_val:
                p_idx -= 1
                a[i], a[p_idx] = a[p_idx], a[i]
        a[p_idx-1], a[low] = a[low], a[p_idx-1]

        return p_idx -1

    def quick_sort_recursive(self, a, low, high):
        if low < high:

            p = self.partition_low(a, low, high)
            self.quick_sort_recursive(a, low, p-1)
            self.quick_sort_recursive(a, p+1, high)

        return a

    def quick_sort_iterative(self, a, low, high):

        stack = [0] * (high-low+1)

        top = -1

        top += 1
        stack[top] = low
        top += 1
        stack[top] = high

        while top >= 0:
            h = stack[top]
            top -= 1
            l = stack[top]
            top -= 1

            p = self.partition_high(a, l, h)

            if p-1 > l:
                top += 1
                stack[top] = low
                top += 1
                stack[top] = p - 1

            if p+1 < h:
                top += 1
                stack[top] = p + 1
                top += 1
                stack[top] = h

        return a

    def heapify(self, a, n, i):
        lc = 2 * i + 1
        rc = 2 * i + 2

        max_idx = i

        if lc < n and a[lc] > a[max_idx]:
            max_idx = lc

        if rc < n and a[rc] > a[max_idx]:
            max_idx = rc

        while max_idx != i:
            a[i], a[max_idx] = a[max_idx], a[i]
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

        s = len(a) // 2

        while s > 0:
            for i in range(len(a)):
                cur_idx = i
                cur_val = a[i]
                while cur_idx >= s and a[cur_idx-s] > cur_val:
                    a[cur_idx] = a[cur_idx-s]
                    cur_idx -= s
                a[cur_idx] = cur_val
            s //= 2

        return a

    def counting_sort(self, a):

        mx = max(a)

        res = [0] * len(a)
        cnt = [0] * (mx+1)

        for ele in a:
            cnt[ele] += 1

        cnt[0] -= 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i-1]

        for i in reversed(a):
            res[cnt[i]] = i
            cnt[i] -= 1

        return res

    def counting_sort_ranged(self, a):
        mn = min(a)
        mx = max(a)

        res = [0] * len(a)
        cnt = [0] * (mx - mn + 1)

        for ele in a:
            cnt[ele-mn] += 1

        cnt[0] -= 1
        for i in range(1, len(cnt)):
            cnt[i] += cnt[i-1]

        for ele in reversed(a):
            res[cnt[ele-mn]] = ele
            cnt[ele-mn] -= 1

        return res

    def bucket_sort(self, a):

        res = []
        buckets = dict()
        for i in range(10):
            buckets[i] = []

        for ele in a:
            buckets[ele//10].append(ele)

        for key, item in buckets.items():
            self.insertion_sort(item)
            res += item

        return res

    def counting_sort_for_radix_sort(self, a, base):
        res = [0] * len(a)
        cnt = [0] * 10

        for ele in a:
            cnt[ele//base % 10] += 1

        cnt[0] -= 1
        for i in range(1, 10):
            cnt[i] += cnt[i-1]

        for ele in reversed(a):
            res[cnt[ele//base%10]] = ele
            cnt[ele // base % 10] -= 1

        return

    def radix_sort(self, a):

        base = 1
        while base < max(a):
            self.counting_sort_for_radix_sort(a, base)
            base *= 10
        return a



a = [64, 34, 25, 12, 22, 11, 90]
b = [3, 5, 6]
solver = Solution()
print('original a:', a)

print('selection_sort_iterative:', solver.selection_sort_iterative(a))
# print('selection_sort_rec:', solver.selection_sort_rec(a, 0, len(a)-1))
print('bubblesort:    ', solver.bubble_sort(a))
print('insertion_sort:', solver.insertion_sort(a))
print('merge_sort:    ', solver.merge_sort(a, 0, len(a)-1))
print('quick_sort:', solver.quick_sort_recursive(a, 0, len(a)-1))
print('quick_sort:', solver.quick_sort_iterative(a, 0, len(a)-1))
# print('heap_sort:', solver.heap_sort(b))
print('shell_sort:', solver.shell_sort(a))
print('counting_sort:', solver.counting_sort(a))
print('counting_sort:', solver.counting_sort_ranged(a))
print('bucket_sort:', solver.bucket_sort(a))
print('radix_sort:', solver.radix_sort(a))
