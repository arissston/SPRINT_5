import random
import string


def generate_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@test.ru"


def generate_password(length=8):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
