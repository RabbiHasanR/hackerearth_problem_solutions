n = int(input())
list_one = list(map(int, input().split()))
list_two = list(map(int, input().split()))
count = 0
i = 0
min_list_one = min(list_one)

while(i<n):
    while(list_one[i]>min_list_one):
        list_one[i] = list_one[i] - list_two[i]
        count+=1
        if list_one[1]<0:
            count = -1
            i = n
            break
        if list_one[i] < min_list_one:
            min_list_one = list_one[i]
            i = -1
            break
    i+=1
print(count)