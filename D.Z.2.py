import random


def get_numbers_ticket(min, max, quantity):
    # Перевірка валідності вхідних параметрів
    if min < 1:
        return []
    if max > 1000:
        return []
    if min >= max:
        return []
    if quantity > (max - min + 1):  # Кількість не може перевищувати діапазон
        return []

    # Генеруємо унікальні випадкові числа за допомогою множини
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    # Повертаємо відсортований список
    return sorted(numbers)


# Тестування
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)