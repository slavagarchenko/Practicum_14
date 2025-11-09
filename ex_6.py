number = int(input("Введите число: "))

if number == 0:
    print("Бесконечное число делителей")

else:
    number = abs(number)
    dividers = []

    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            dividers.append(i)
            if i != number // i:
                dividers.append(number // i)

    dividers.sort()
    print(dividers)
