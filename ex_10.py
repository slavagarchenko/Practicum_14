first_list = list(map(int, input("Введите первый список чисел: ").split()))
second_list = list(map(int, input("Введите второй список чисел: ").split()))
start, end = map(int, input("Введите диапозон: ").split())

if start > end:
    start, end = end, start

start = max(1, min(start, len(first_list))) - 1
end = max(1, min(end, len(first_list))) - 1

for i in range(end, start-1, -1):
    second_list.append(first_list[i])

for i in range(end, start-1, -1):
    del first_list[i]

print(first_list)
print(second_list)
