import bcrypt
from utils.db_manager import add_user, email_exists


def register_user(full_name, email, password):

    if email_exists(email):
        return False, "Email already exists!"

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

    add_user(
        full_name,
        email,
        hashed_password.decode()
    )

    return True, "Registration Successful!"