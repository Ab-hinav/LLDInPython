import random
import string

def generate_id(prefix: str, length: int = 6) -> str:
    characters = string.ascii_uppercase + string.digits
    random_part = ''.join(random.choices(characters, k=length))
    return f"{prefix}_{random_part}"

