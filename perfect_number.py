t = int(input())
nums = []
for i in range(t):
    nums.append(int(input()))

def perfect_numer(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

for n in nums:
    if perfect_numer(n):
        print('YES')
    else:
        print('NO')