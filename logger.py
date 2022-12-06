from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            text = f"время вызова функции: {datetime.now()}\n" \
                   f"имя функции: {old_function.__name__}\n" \
                   f"возвращаемый результат поиска вакансий: {result}\n\n"
            with open(path, "a", encoding="utf-8") as file:
                file.write(text)
            return result
        return new_function
    return __logger

