"""Исключения."""


class TypeDataError(Exception):
    """Исключение для типа."""

    def __init__(self, message, errors_list):
        """Инициализация."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list if errors_list else ["unknown"]

    def __str__(self):
        """Текст ошибки."""
        return "присланный объект - не список списков: " + ", ".join(self.errors_list)


class NoRectangleError(Exception):
    """Исключение для прямоугольника."""

    def __init__(self, message, errors_list):
        """Инициализация."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list if errors_list else ["unknown"]

    def __str__(self):
        """Текст ошибки."""
        return "присланный двумерный список - не прямоугольный: " + ", ".join(self.errors_list)


class EmptyError(Exception):
    """Исключение для пустоты."""

    def __init__(self, message, errors_list):
        """Инициализация."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list if errors_list else ["unknown"]

    def __str__(self):
        """Текст ошибки."""
        return "присланный список пуст: " + ", ".join(self.errors_list)


class ElError(Exception):
    """Исключение для элементов."""

    def __init__(self, message, errors_list):
        """Инициализация."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list if errors_list else ["unknown"]

    def __str__(self):
        """Текст ошибки."""
        return "в присланном двумерном списке присутствуют элементы которые не являются нулем либо единицей.: " + \
               ", ".join(self.errors_list)
