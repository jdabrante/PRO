def num_divisor (num: int):
    count = 2
    target = num//2
    for n in range(2,target+1):
        if num%n == 0:
            count += 1
    return count

print(num_divisor(1024))