import re

def contains_secret(text):
    return bool(re.search(r"ctf\{[^}]+\}", text))
