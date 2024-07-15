from typing import Optional
import string

__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    ts = text.strip(string.punctuation+string.whitespace)
    if len(ts) == 0:
        return (None, None)
    for s in string.punctuation+string.whitespace:
        ts = ts.replace(s, ' ')
    # End for
    slList = ts.split()
    return (min(slList, key=len), max(slList, key=len))
    # raise NotImplementedError
