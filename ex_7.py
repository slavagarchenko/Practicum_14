numbers = list(map(int, input("Введите список чисел: ").split()))

total_sum = sum(numbers)
even_sum = sum(num for num in numbers if num % 2 == 0)
odd_sum = total_sum - even_sum

print(f"Сумма четных: {even_sum}, сумма нечетных: {odd_sum}")
