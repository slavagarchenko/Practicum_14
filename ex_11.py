numbers = list(map(int, input("Введите список чисел: ").split()))
comand = input("Введите команду для сдвига: ")
current_list = []

while comand[0].lower() not in ["r", "l"] or not comand[1:].isdigit():
    comand = input("Введите коректную команду: ")

direction = comand[0].lower()
step = int(comand[1:]) % len(numbers)

if direction == "r":
    step = len(numbers) - step

current_list = numbers[step:] + numbers[:step]

print(current_list)
