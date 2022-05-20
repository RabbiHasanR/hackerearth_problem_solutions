n = int(input())

for i in range(n):
    x,y,a,b = (input()).split()
    if (int(x)*int(y))== (int(a)+int(b)):
        print('Yes')
    else:
        print('No')
