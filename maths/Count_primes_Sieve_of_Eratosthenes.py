class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primecount = 0
        isprime = [True] * n
        isprime[0] = False
        isprime[1] = False
        
        for i in range(2, int(n**0.5)+1):
            if (isprime) == False:
                continue
            else:
                for j in range(i*i, n, i):
                    isprime[j] = False
                
        for i in range(2, n):
            if (isprime[i]) == True:
                primecount += 1
                
        return primecount