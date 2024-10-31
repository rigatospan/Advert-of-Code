def perm_s(s: str, nums: list[int], memo: dict):
    # count the valid permutations for current s and nums
    count = 0

    # if s is empty check if there are any numbers left; otherwise is a valid permutation
    if s == '':
        return 1 if nums == () else 0
    
    # if the numbers are empty check if '#' is in s; 
    # if not all remaining '?' should be '.' and is a valid permutation 
    if nums == ():
        return 1 if '#' not in s else 0
    
    configuration = (s, nums)
    if configuration in memo:
        return memo[configuration]
    
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
    
    memo[configuration] = count
                
    return count

result = 0

for line in open('d12_23.txt').read().splitlines():
    s, n = line.split(' ')
    
    # update what are the strings and numbers now
    numbers = tuple([int(a) for a in n.split(',')]*5)
    s = '?'.join([s]*5)
    
    # use a memo dictionary to store the (s, nums) pairs that already solved
    memo = {}
    res= perm_s(s, numbers, memo)
    result+=res
    
print(f'result is {result}')