def get_primes(nums: list):
    for num in nums:
        is_prime = True
        for x in range(2, num):
            if num % x == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))