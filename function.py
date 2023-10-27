def find_max(nunbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

find_max([1,2,3,4,5])
