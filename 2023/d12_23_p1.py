def perm_s(s: str, nums: list[int], memo):
    # count the valid permutations for current s and nums
    count = 0

    # if s is empty check if there are any numbers left; otherwise is a valid permutation
    if s == '':
        return 1 if nums == () else 0
    
    # if the numbers are empty check if '#' is in s; 
    # if not all remaining '?' should be '.' and is a valid permutation 
    if nums == ():
        return 1 if '#' not in s else 0
    
    # check if we solve this problem already
    if (s, nums) in memo:
        return memo[(s, nums)]
    
    # consider the first character and the first number
    # if the character is a '.' or '?' considered as '.'
    if s[0] in '.?':
        count += perm_s(s[1:], nums, memo)
    
    # if the character is a '#' or '?' considered as '#'
    if s[0] in '#?':
        if '.' not in s[0:nums[0]]:
            if len(s) == nums[0]: 
                count += perm_s(s[nums[0]+1:], nums[1:], memo)
            elif len(s) > nums[0] and s[nums[0]] != '#':
                count += perm_s(s[nums[0]+1:], nums[1:], memo)
    
    # add the solution of the problem to the memo dict
    memo[(s, nums)] = count
    
    return count

result = 0

for line in open('d12_23.txt').read().splitlines():
    s, n = line.split(' ')
    numbers = tuple([int(a) for a in n.split(',')])
    
    # use a memo dictionary to store the (s, nums) pairs that already solved
    memo = {}
    result += perm_s(s, numbers, memo)

print(f'result is {result}')