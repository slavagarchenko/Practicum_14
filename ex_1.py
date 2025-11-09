old_list = []
new_list = []

for i in range(10):
    number = int(input("Введите число: "))
    old_list.append(number)

for i in range(8):
    new_list.append(old_list[i] + old_list[i+1])

print(new_list)
