def solve (A, N):
    # Write your code here
    middle = int(N / 2)
    first_digits = [int(str(i)[0])for i in A[:middle]]
    second_digits = [int(str(i)[-1])for i in A[middle:]]
    number_one = ''.join([str(i) for i in first_digits])
    number_two = ''.join([str(i) for i in second_digits])

    if int(number_one+number_two) % 11 == 0:
        return 'OUI'
    return 'NON'

N = int(input())
A = list(map(int, input().split()))

out_ = solve(A, N)
print (out_)