__all__ = ("is_prime",)


def is_prime(number: int) -> bool:
    """Определяет, является ли число простым.

    Example:
        >> is_prime(0):
        False
        >> is_prime(1):
        False
        >> is_prime(4):
        True
    """
    # Алгоритм из https://wiki.algocode.ru/index.php?title=Проверка_на_простоту_за_корень
    if number == 0 or number == 1:
        return False
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        # End if
        i = i+1
    # End for
    return True
    # raise NotImplementedError
