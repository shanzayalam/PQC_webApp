# app/crypto_utils.py

from kyber_py.kyber import Kyber512
import base64

# Helper functions for base64 encoding/decoding
def encode(data: bytes) -> str:
    return base64.b64encode(data).decode('utf-8')

def decode(data_str: str) -> bytes:
    return base64.b64decode(data_str.encode('utf-8'))

# Generate public and private keys (returns base64-encoded strings)
def generate_keys():
    public_key, private_key = Kyber512.keygen()
    return {
        'public_key': encode(public_key),
        'private_key': encode(private_key)
    }

# Encrypt message using the public key
def encrypt_message(message: str, public_key_b64: str) -> dict:
    try:
        public_key = decode(public_key_b64)
        shared_secret, ciphertext = Kyber512.encaps(public_key)
        return {
            'ciphertext': encode(ciphertext),
            'shared_secret': encode(shared_secret)
        }
    except Exception as e:
        return {'error': str(e)}

# Decrypt ciphertext using the private key
def decrypt_message(ciphertext_b64: str, private_key_b64: str) -> dict:
    try:
        ciphertext = decode(ciphertext_b64)
        private_key = decode(private_key_b64)
        shared_secret = Kyber512.decaps(private_key, ciphertext)
        return {
            'shared_secret': encode(shared_secret)
        }
    except Exception as e:
        return {'error': str(e)}
