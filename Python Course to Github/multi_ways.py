nums = [1,2,3,4,5,6,7,8,9,10]
#<------- Filter Way ------->#
""" 
def even(num):
    return num%2

evenNums = list(filter(even, nums))
print(evenNums)

#<------- Comprehension Way ------->#

nums = [num for num in nums if num%2+==0]
print(nums)

#<------- Traditoinal Way ------->#

evenNums = []
for num in nums:
    if num%2 == 0:
        evenNums.append(num)

print(evenNums)

#<------- Lambda Way ------->#

evenNums = list(filter(lambda num: num%2==0,nums))
print(evenNums) 

"""