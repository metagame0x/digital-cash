from ecdsa import SigningKey, SECP256k1

alice_private_key = SigningKey.from_secret_exponent(1, curve=SECP256k1)
alice_public_key = alice_private_key.get_verifying_key()

bob_private_key = SigningKey.from_secret_exponent(2, curve=SECP256k1)
bob_public_key = bob_private_key.get_verifying_key()

def user_private_key(name):
    name_to_key = {
        "alice": alice_private_key,
        "bob": bob_private_key,
    }
    return name_to_key[name]

def key_to_name(key):
    key_to_name_map = {
        alice_private_key.to_string(): "alice_private_key",
        alice_public_key.to_string(): "alice_public_key",
        bob_private_key.to_string(): "bob_private_key",
        bob_public_key.to_string(): "bob_public_key",
    }
    return key_to_name_map[key.to_string()]

def user_public_key(name):
    private_key = user_private_key(name)
    return private_key.get_verifying_key()

def node_private_key(id):
    assert isinstance(id, int)
    assert id >= 0
    base = 1000  # So bank keys don't collide with user keys ...
    return SigningKey.from_secret_exponent(base + id, curve=SECP256k1)

def node_public_key(id):
    """Returns public key of a block producer given their ID"""
    private_key = node_private_key(id)
    return private_key.get_verifying_key()
