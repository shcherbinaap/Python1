#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_num = int(input("Введите положительное число: "))
max_num = 0
n = 0
while True:
    num = int((user_num / (10**n)) % 10)
    if num == 0:
        break
    elif num > max_num:
        max_num = num
    n += 1
print(max_num)