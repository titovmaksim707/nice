n = int(input())
numbers = [int(input()) for _ in range(n)]

# Отфильтровать числа, кратные 5, и найти максимальное
max_multiple = max(num for num in numbers if num % 5 == 0)
print(max_multiple)
