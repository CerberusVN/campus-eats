USERS = []


def register(email):
    """FR-ACC-001: register a user with a unique email."""
    if email in USERS:
        raise ValueError("Email already registered")
    USERS.append(email)
    return email
