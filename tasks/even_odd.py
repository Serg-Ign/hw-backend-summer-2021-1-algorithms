__all__ = ("even_odd",)


def even_odd(numbers: list[int]) -> float:
    """Определяет отношение суммы четных элементов списка
    к сумме нечетных.

    Example:
        >> even_odd([1, 2, 3, 4, 5])
        0.6667
    """
    # Проверка валидности граничных условй (по тестам):
    #   - пустой массив (список): результат 0.0
    arr = []
    arr = numbers
    if not arr:
        return 0.0

    iEvenNumSum = 0  # Сумма четных чисел списка
    iOddNumSum = 0  # Сумма нечетных чисел
    for num in arr:
        if num % 2 == 0:
            iEvenNumSum += num
        else:
            iOddNumSum += num
        # end if
    # end for

    #   - в массиве только четные значения : результат 0.0 (ХХХ/0 на ноль делить нельзя)
    #   - в массиве только один/несколько нулевых элементов : результат 0.0 (частный случай только четных чисел)
    if iOddNumSum == 0:
        return 0.0
    else:
        return iEvenNumSum / iOddNumSum
    # raise NotImplementedError
