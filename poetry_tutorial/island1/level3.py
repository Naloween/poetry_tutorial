
def is_acceptable_password(password: str) -> bool:
    """tells if a password is acceptable

    Args:
        password (str): the password to test

    Returns:
        bool: is the password acceptable
    """
    return len(password) > 6
