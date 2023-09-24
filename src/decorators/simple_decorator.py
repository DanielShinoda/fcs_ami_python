import time

from clock.decorator_clock import clock


@clock
def snooze(seconds) -> None:
    time.sleep(seconds)


@clock
def factorial(n: int) -> int:
    return 1 if n < 2 else n * factorial(n - 1)


if __name__ == "__main__":
    print("*" * 40, "Calling snooze(.123)")
    snooze(0.123)
    print("*" * 40, "Calling factorial(6)")
    print("6! =", factorial(6))


# Очерёдность действий в clocked:
# 1. Записывает начальное время t0
# 2. Вызывает оригинальную функцию factorial, сохраняя результат
# 3. Вычисляет прошедшее время
# 4. Форматирует и выводит собранные данные
# 5. Возвращается к шагу 2
