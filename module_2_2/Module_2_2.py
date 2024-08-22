first = int(input("введите первое число "))
second = int(input("введите второе число "))
third = int(input("введите третье число "))
if first == second and second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
else:
    print(2)
