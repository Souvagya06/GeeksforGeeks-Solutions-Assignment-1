class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        last_non_zero = 0  # Pointer for placing the next non-zero element

        for i in range(n):
            if arr[i] != 0:
                arr[last_non_zero], arr[i] = arr[i], arr[last_non_zero]
                last_non_zero += 1
        return arr