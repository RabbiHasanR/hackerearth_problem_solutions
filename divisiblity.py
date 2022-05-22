N = int(input())
data = [int(x) for x in input().split()]

last_digit_number = int(''.join([str(i)[-1] for i in data]))
ans = 'No'
if last_digit_number % 10 == 0:
    ans = 'Yes'

print(ans)