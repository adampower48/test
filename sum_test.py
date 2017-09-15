import random


def gen_rands(n, _min, _max):
    nums = []
    for _ in range(n):
        nums.append(random.randrange(_min, _max))
    return nums


def _sum(nums):
    tot = 0
    for num in nums:
        tot += num
    return tot


total = 0
for i in range(1000):
    total += _sum(gen_rands(i, 0, i))

print total
