n = int(input())

for i in range(n):
    result = 0
    row, column = (input()).split()
    for a in range(int(row)):
        border = input()
        borders = [i for i in border.split('.') if len(i) > 0 and i == len(i) * i[0]]
        if len(borders)>0:
            border_result = len(max(borders, key=len))
            if border_result > result:
                result = border_result
    print(result)
