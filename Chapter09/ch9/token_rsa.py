import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


data = {'payload': 'data'}


def encode(data, priv_filename, priv_pwd=None, algorithm='RS256'):

    with open(priv_filename, 'rb') as key:
        private_key = serialization.load_pem_private_key(
            key.read(),
            password=priv_pwd,
            backend=default_backend()
        )

    return jwt.encode(data, private_key, algorithm=algorithm)


def decode(data, pub_filename, algorithm='RS256'):

    with open(pub_filename, 'rb') as key:
        public_key = key.read()

    return jwt.decode(data, public_key, algorithm=algorithm)


# no pwd
token = encode(data, 'rsa/key')
data_out = decode(token, 'rsa/key.pub')
print(data_out)


# with pwd
token = encode(data, 'rsa/keypwd', priv_pwd=b'Password123')
data_out = decode(token, 'rsa/keypwd.pub')
print(data_out)
