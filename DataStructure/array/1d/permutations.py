# Problem
# You are given a permutation with length . You want to play a game with you friend, Bob, and the rule will be as follows: 

# You will choose a subarray  from the permutation. Then, ask Bob to find the maximum element in the rest of the numbers.
# You are given a permutation  contains all numbers  to . And, in  queries, each query has two integers  and .

# For each query, you have to help Bob find the maximum value that does not exist in the subarray .

# Note: A permutation is a sequence of integers from  to  of length  containing each number exactly once. 
# For example, (1), (4, 3, 5, 1, 2), (3, 2, 1) are permutations and (1, 1), (4, 3, 1), (2, 3, 4) are not.

# Input format

# The first line contains two integers  and  denoting the number of elements and the number of test cases. 
# The second line contains  space-separated integers.
# The next  lines and each line contains two integers , .
# Output format

# Print the maximum number that does not exist in the subarray .

# Constraints

# Sample Input
# 5 3
# 2 3 1 5 4
# 1 2
# 2 4
# 2 5
# Sample Output
# 5
# 4
# 2
# Time Limit: 2
# Memory Limit: 256
# Source Limit:
# Explanation
# In the sample, we have a permutation  (2, 3, 1, 5, 4)

# the first test-case [l,r] = [1,2] so we have to find the maximum number of the array except for the subarray [1,2]

# in other words, we have to find the maximum number for the subarray [3,5] which will be 5. 


name = input().split() 
t = input().split()
 
l = len(t)
for i in range(l):
    t[i] = int(t[i])
 
queries = []
for i in range(int(name[1])):
    temp = input().split()
    queries.append([int(temp[0]),int(temp[1])])
 
q_l = len(queries)
 
prefix_array = [1 for i in range(l+2)]
suffix_array = [1 for i in range(l+2)]
# print('queris_len:',q_l,'prfix_array:',prefix_array,'suffix_array:',suffix_array, 'queris:',queries, 'name:',name)
for i in range(2,l+1):
    prefix_array[i] = (max(prefix_array[i-1],t[i-2]))
 
for i in range(l-1,0,-1):
    suffix_array[i] = max(suffix_array[i+1],t[i])
 
# print(prefix_array, suffix_array)
for i in range(q_l):
    print(max(prefix_array[queries[i][0]], suffix_array[queries[i][1]]))