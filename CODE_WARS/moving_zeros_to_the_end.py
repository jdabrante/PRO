# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    messy = True
    while messy:
        messy = False
        for i in range(len(lst)-1):
            if lst[i] == 0 and lst[i + 1] != 0:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                messy = True
    return lst

# def move_zeros(array):
#     for i in array:
#         if i == 0:
#             array.remove(i) # Remove the element from the array
#             array.append(i) # Append the element to the end
#     return array