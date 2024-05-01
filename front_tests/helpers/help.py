import random
import string


def random_string(length: int = 10) -> str:
    """Генерация рандомной строки"""
    return "".join([random.choice(string.ascii_letters) for _ in range(length)])


def random_email() -> str:
    """Генерация рандомного e-mail"""
    return random_string() + "@" + random_string(5) + "." + random.choice(["com", "ua", "org", "ru"])


def locator_with_contains(locator, value):
    """Дополнение локатора содержащимся текстом"""
    method, element = locator
    return method, f"{element}[contains(text(), '{value}')]"
