import bcrypt
from utils.db_manager import (
    add_user,
    email_exists,
    get_user_by_email
)

# -------------------------
# Register User
# -------------------------
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


# -------------------------
# Login User
# -------------------------
def login_user(email, password):

    user = get_user_by_email(email)

    if user is None:
        return False, "Email not found!"

    stored_password = user[3]

    if bcrypt.checkpw(
        password.encode(),
        stored_password.encode()
    ):
        return True, user

    return False, "Incorrect Password!"