import re


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер починається з '+' — залишаємо як є
    if cleaned.startswith("+"):
        return cleaned

    # Якщо номер починається з '380' — додаємо лише '+'
    if cleaned.startswith("380"):
        return "+" + cleaned

    # Якщо номер починається з '0' — додаємо '+38'
    if cleaned.startswith("0"):
        return "+38" + cleaned

    # В інших випадках — додаємо '+38'
    return "+38" + cleaned


# Тестування
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)