from Argon2 import PasswordHasher




ph = PasswordHasher()


def hash_password(password):
    return ph.hash(password)

def verify_password(stored_password, provided_password):
    try:
        ph.verify(stored_password, provided_password)
        return True
    except:
        return False
