def str_upper(string: str):
    """
    Функция выводит строку в верхнем регистре
    """
    return string.upper()

def str_title(string: str):
    """
    Функция выводит строку с заглавными буквами в словах
    """
    str_list = string.split(' ')
    str_list = [word.title() for word in str_list]
    return ' '.join(str_list)