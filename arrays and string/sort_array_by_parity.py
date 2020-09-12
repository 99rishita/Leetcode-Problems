class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        k = 0
        for i in range(len(A)):
            if A[i]%2 == 0:
                A[k], A[i] = A[i], A[k]
                k += 1
        return A
        