# 欧拉筛求范围内所有质数:
class Primes:
    def __init__(self, n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p): primes[i] = False
            p += 1
        self.prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    def get_primes(self):
        return self.prime_numbers
    @cache
    def get_prime_factors(self, n):
        factors, i = [], 0
        while i < len(self.prime_numbers) and self.prime_numbers[i] ** 2 <= n:
            if n % self.prime_numbers[i]: i += 1
            else:
                n //= self.prime_numbers[i]
                factors.append(self.prime_numbers[i])
        if n > 1: factors.append(n)
        return factors

# 将 10 进制数字转换为任意的 k进制字符串:
def convert_to_base_k(number: int, k: int) -> str:
    if number == 0:
        return '0'
    flag = '-' if number < 0 else ''
    number = abs(number)
    result = ''
    while number > 0:
        number, remainder = divmod(number, k)
        result = str(remainder) + result
    return flag + result