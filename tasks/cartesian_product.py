from typing import TypeVar

__all__ = ("cartesian_product",)


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def cartesian_product(arr1: list[T1], arr2: list[T2]) -> list[tuple[T1, T2]]:
    """Определяет декартово произведение двух списков.

    Example:
        >> cartesian_product([1, 2], [3, 4])
        [(1, 3), (1, 4), (2, 3), (2, 4)]
    """
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if type(arr1[i]) != list:
                arr1[i] = [arr1[i]]
            temp = [num for num in arr1[i]]
            temp.append(arr2[j])
            result.append(temp)
        # End for j
    # End for i
    lstTuple = []
    for lst in result:
        lstTuple.append(tuple(lst))
    return lstTuple
    # raise NotImplementedError
