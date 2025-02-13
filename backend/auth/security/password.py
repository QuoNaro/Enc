from settings import PWD_CONTEXT

def verify_password(
    plain_password: str, 
    hashed_password: str
) -> bool:
    """
    Проверяет соответствие открытого пароля его хэшу.

    Parameters:
        plain_password (str): Открытый пароль.
        hashed_password (str): Хэшированный пароль.

    Returns:
        bool: True если пароли совпадают, иначе False.
    """
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_password_hash(
    password: str
) -> str:
    """
    Создает хэш для заданного пароля.

    Parameters:
        password (str): Пароль для хэширования.

    Returns:
        str: Хэшированный пароль.
    """
    return PWD_CONTEXT.hash(password)


__all__ = ["get_password_hash"]
