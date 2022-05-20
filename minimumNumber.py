n = int(input())
numbers = [int(num) for num in input().split(" ", n-1)]
print(numbers)
print(min(numbers))