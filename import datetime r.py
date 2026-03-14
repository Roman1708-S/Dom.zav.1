from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Повертає кількість днів між заданою датою (у форматі 'YYYY-MM-DD')
    та поточною датою. Якщо задана дата пізніша за поточну, результат
    буде від'ємним.

    :param date: Рядок дати у форматі 'YYYY-MM-DD'
    :return: Ціле число днів (може бути від'ємним)
    """
    try:
        # Парсимо вхідний рядок у об'єкт date (без часу)
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        # Якщо формат некоректний, піднімаємо зрозуміле виключення
        raise ValueError("Дата має бути у форматі 'YYYY-MM-DD'")

    # Поточна дата (також без часу)
    today = datetime.today().date()

    # Різниця у днях (ціле число, може бути від'ємним)
    delta = today - target_date
    return delta.days
print(get_days_from_today("2026-12-17"))