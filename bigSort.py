# Online Python compiler (interpreter) to run Python online.
# 2
# 3 2 3
# 2 4 1
# 3 1 5
# 2 2 2
# 9 5
# 1 2

# output
# 2 1 4
# 5 9

# 2
# 3 4 2
# 2 9 6
# 3 9
# 4 4 3
# 5 7 11 6
# 4 10 15

# output
# 2 9
# 6 7 11

from sys import int_info


def bigSort(packet, x, query):
    packets = packet * x
    packets.sort()
    result = []
    for i in query:
        result.append(packets[i])
    return result

t = int(input())

results = []

for i in range(t):
    n, x, q = input().split()
    packte = [int(i) for i in input().split(' ', int(n)-1)]
    query = [int(i) for i in input().split(' ', int(q)-1)]
    results.append(bigSort(packte, int(x), query))

for r in results:
    print(*r)