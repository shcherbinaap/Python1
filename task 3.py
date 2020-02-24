#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_num = input("Введите число: ")

n = user_num
nn = user_num * 2
nnn = user_num * 3

print(int(n) + int(nn) + int(nnn))