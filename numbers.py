from statistics import median, mode, multimode

numbers = [10,23,24,56,78,90,23,45,45]

add = sum(numbers)
avg = sum(numbers)/len(numbers)
middle_num = median(numbers)
mode_num = mode(numbers)

print(add, avg, mode_num, middle_num)