from passlib.context import CryptContext


# --------------------------------------------------


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    """A class for hashing and verifying passwords.

    Args:
        pwd_context: The password hashing context.
    """

    def hash_password(password):
        """Hash a password.

        Args:
            password: The password to be hashed.

        Returns:
            The hashed password.
        """

        return pwd_context.hash(password)


    def verify_password(plain_password, hashed_password):
        """Verify a password.

        Args:
            plain_password: The password to be verified.
            hashed_password: The hashed password to be verified against.

        Returns:
            True if the password is valid, False otherwise.
        """

        return pwd_context.verify(plain_password, hashed_password)