numbers = list(map(int, input("Введите список чисел: ").split()))

if len(numbers) != 0:
    print(sum(numbers)/len(numbers))
else:
    print(0)
