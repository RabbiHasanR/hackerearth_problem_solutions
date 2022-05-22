N = int(input())

village = input()

village = village.replace('.', 'B')
isPossible = True

for i in range(0, N-1):
    if village[i] == 'H' and village[i+1] == 'H':
        print('NO')
        isPossible=False
        break
if isPossible:
    print('YES')
    print(village)