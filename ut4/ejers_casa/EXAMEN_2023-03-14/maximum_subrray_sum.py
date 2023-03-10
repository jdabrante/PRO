# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]

# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

# def max_sequence(numbers: list, max_sum: int = 0)-> int:
#     _sum = 0
#     if len(numbers) == 0:
#         return max_sum
#     for number in numbers: 
#         _sum += number
#         if _sum > max_sum:
#             max_sum = _sum
#     return max_sequence(numbers[1:], max_sum)


def comparation (numbers: list, max_sum: int)->bool:
    if sum(numbers) > max_sum:
        return True
    return False

def max_sequence(numbers: list, max_sum: int = 0)-> int: 
    while True:
        if len(numbers) == 0:
            return max_sum
        if comparation(numbers,max_sum):
            max_sum = sum(numbers)
        if comparation(numbers[1:], max_sum):
            max_sum = sum(numbers[1:])
        if comparation(numbers[:len(numbers)-1], max_sum):
            max_sum = sum(numbers[:len(numbers)-1])
        numbers = numbers[1:len(numbers)-1]
    
