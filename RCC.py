print("введите два числа:")

a = int(input())
b = int(input())

if a >= b:
    print(a)
else:
    print(b)

print("выводим разность квадратов:")
print((a - b)*(a + b))
print("выводим сумму квадратов:")
print(a * a + b * b)
print('вывод квадрата разности:')
print((a - b)*(a - b))
print('выводим квадрат суммы:')
print((a + b)*(a + b))


