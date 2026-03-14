from datetime import datetime

def get_days_from_today(date):
    try:
        # 1. Перетворюємо рядок у об'єкт datetime
        # Використовуємо формат '%Y-%m-%d' (РРРР-ММ-ДД)
        given_date = datetime.strptime(date, '%Y-%m-%d')
        
        # 2. Отримуємо поточну дату
        # .today() повертає час, тому ми перетворюємо його на об'єкт .date() 
        # або просто працюємо з datetime, ігноруючи години/хвилини пізніше
        today = datetime.today()
        
        # 3. Розраховуємо різницю (результатом буде об'єкт timedelta)
        difference = today - given_date
        
        # 4. Повертаємо кількість днів як ціле число (.days)
        return difference.days
        
    except ValueError:
        # Обробка помилки, якщо формат дати неправильний
        return "Неправильний формат дати. Очікується 'РРРР-ММ-ДД'."

# Приклади використання:
print(get_days_from_today('2021-10-0git init9'))  # Кількість днів від минулої дати
print(get_days_from_today('2026-12-31'))  # Від'ємне число для майбутньої дати``