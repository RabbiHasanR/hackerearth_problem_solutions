def FindIt (arr):
    # Write your code here
    return min(arr)
 
n = int(input())
arr = list(map(int, input().split()))
 
out_ = FindIt(arr)
print (out_)