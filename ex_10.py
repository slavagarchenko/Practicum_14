first_list = list(map(int, input("Введите первый список чисел: ").split()))
second_list = list(map(int, input("Введите второй список чисел: ").split()))
start, end = map(int, input("Введите диапозон: ").split())

if start > end:
    start, end = end, start

start = max(1, min(start, len(first_list)))
end = max(1, min(end, len(first_list)))

elements_to_move = first_list[start - 1:end][::-1]
second_list.extend(elements_to_move)
del first_list[start - 1:end]

print(first_list)
print(second_list)
