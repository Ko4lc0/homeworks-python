first = int(input("введите первое число "))
second = int(input("введите второе число "))
third = int(input("введите третье число "))
if first == second and second == third:
    print(3)
elif first == second and first != third or first == third and first != second:
    print(2)
else:
    print(0)

