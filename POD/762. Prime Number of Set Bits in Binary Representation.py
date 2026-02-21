class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def isprime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes = {i for i in range(2, 33) if isprime(i)}
        count = 0
        for i in range(left, right+1):
            b = bin(i)[2:]
            v = b.count("1")
            if v in primes:
                count += 1
        return count
