def log(filename=None):
    """декоратор лоирования функции"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            # Логируем начало выполнения
            start_message = f"Начало выполнения функции {func.__name__}."
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_message + "\n")
            else:
                print(start_message)

            try:
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                success_message = f" {func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                # Логируем ошибку
                error_message = f"{func.__name__} error {type(e).__name__} " f" inputs: {args}, {kwargs}."
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise  # Повторно вызываем исключение

        return wrapper

    return decorator
