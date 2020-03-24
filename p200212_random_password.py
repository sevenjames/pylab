"""
simple random password generator

"""

import string
import secrets

def make_pass(length):
    """Generate a random password of given length."""
    alphabet = string.ascii_letters + string.digits
    password = str().join(secrets.choice(alphabet) for i in range(length))
    return password
