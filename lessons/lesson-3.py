def average (numbers, k=None):
    if k == None:
        k = len(numbers)
    return sum(numbers[:k]) / k

my_list = [2, 4, 6, 4]
result = average(my_list, 2)
print (result)