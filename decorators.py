"""Декораторы."""
from typing import Callable
from time import time
from exception import TypeDataError, ElError, EmptyError, NoRectangleError


def validator(func: Callable) -> Callable:
    """Валидатор."""
    def wrapper(p):
        try:
            result = func(p)
        except (EmptyError, TypeDataError, ElError, NoRectangleError) as exc:
            with open(f"error_log_{time()}.txt", "w") as file:
                file.write(str(exc.errors_list))
            print(exc)
            raise exc
        else:
            return result

    return wrapper
