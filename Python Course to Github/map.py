#<------- Map ------->#

nums = [2,5,6,7,8,9,10]

def mapFunction(num):
    return num*2

print(list(map(mapFunction,nums))) # or newNums = list(map(mapFunction,nums))

print(nums)