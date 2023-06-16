# 欧拉筛求范围内所有质数:
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]
    return prime_numbers
prime_numbers = sieve_of_eratosthenes(10 ** 5 + 1)
# 质因数分解（需要欧拉筛）, 返回 list, 包含重复数字，O(logn)复杂度:
@cache
def get_prime_factors(n):
    factors = []
    i = 0
    while i < len(prime_numbers) and prime_numbers[i] ** 2 <= n:
        if n % prime_numbers[i]:
            i += 1
        else:
            n //= prime_numbers[i]
            factors.append(prime_numbers[i])
    if n > 1:
        factors.append(n)
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