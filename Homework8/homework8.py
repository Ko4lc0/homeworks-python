numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(numbers):
    if numbers[index] > 0:
        print(numbers[index])
        index += 1
    else:
        index += 1
        break
