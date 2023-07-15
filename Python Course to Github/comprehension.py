#<------- Comprehension ------->#
prices = [2000, 1000, 3000, 5000]

""" double_prices = []
for price in prices:
    double_prices.append(price*2) """

double_prices = [price*2 for price in prices] # logic 1st loop 2nd

print(double_prices)

nums = [1,2,3,4,5,6,7,8,9,10]
""" even_double_nums = []
for num in nums:
    if num%2 == 0 :
        even_double_nums.append(num*2) """

even_double_nums=[num*2 for num in nums if num%2 == 0] # condition is last in comprehension way

print(even_double_nums)