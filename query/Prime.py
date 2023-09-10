from functools import *
# 欧拉筛求范围内所有质数:
class Prime:
    def __init__(self, n: int):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p): primes[i] = False
            p += 1
        self.prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]

    def get_primes_list(self) -> list:
        return self.prime_numbers

    @cache
    def get_prime_factors(self, n: int) -> list:
        factors, i = [], 0
        while i < len(self.prime_numbers) and self.prime_numbers[i] ** 2 <= n:
            if n % self.prime_numbers[i]: i += 1
            else:
                n //= self.prime_numbers[i]
                factors.append(self.prime_numbers[i])
        if n > 1: factors.append(n)
        return factors
