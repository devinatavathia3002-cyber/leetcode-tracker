# Last updated: 6/24/2026, 4:42:50 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        def merge(arr, L, M, R):
4            left, right = arr[L:M+1], arr[M+1:R+1]
5            i, j, k = L, 0, 0
6
7            while j < len(left) and k < len(right):
8                if left[j] <= right[k]:
9                    arr[i] = left[j]
10                    j += 1
11                else:
12                    arr[i] = right[k]
13                    k += 1
14                i += 1
15
16            while j < len(left):
17                arr[i] = left[j]
18                j += 1
19                i += 1
20
21            while k < len(right):
22                arr[i] = right[k]
23                k += 1
24                i += 1
25
26        def mergeSort(arr, l, r):
27            if l >= r:
28                return
29            m = (l + r) // 2
30            mergeSort(arr, l, m)
31            mergeSort(arr, m + 1, r)
32            merge(arr, l, m, r)
33
34        mergeSort(nums, 0, len(nums) - 1)
35        return nums