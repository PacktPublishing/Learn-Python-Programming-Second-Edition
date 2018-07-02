# NOT A PYTHON MODULE - DO NOT ATTEMPT TO RUN

>>> import hashlib
>>> h = hashlib.blake2b()
>>> h.update(b'Hash me')
>>> h.update(b' now!')
>>> h.hexdigest()
'56441b566db9aafcf8cdad3a4729fa4b2bfaab0ada36155ece29f52ff70e1e9d'
'7f54cacfe44bc97c7e904cf79944357d023877929430bc58eb2dae168e73cedf'
>>> h.digest()
b'VD\x1bVm\xb9\xaa\xfc\xf8\xcd\xad:G)\xfaK+\xfa\xab\n\xda6\x15^'
b'\xce)\xf5/\xf7\x0e\x1e\x9d\x7fT\xca\xcf\xe4K\xc9|~\x90L\xf7'
b'\x99D5}\x028w\x92\x940\xbcX\xeb-\xae\x16\x8es\xce\xdf'
>>> h.block_size
128
>>> h.digest_size
64
>>> h.name
'blake2b'

>>> hashlib.blake2b(b'Hash me now!').hexdigest()
'56441b566db9aafcf8cdad3a4729fa4b2bfaab0ada36155ece29f52ff70e1e9d'
'7f54cacfe44bc97c7e904cf79944357d023877929430bc58eb2dae168e73cedf'
>>> hashlib.sha256(b'Hash me now!').hexdigest()
'10d561fa94a89a25ea0c7aa47708bdb353bbb062a17820292cd905a3a60d6783'

>>> dk = hashlib.pbkdf2_hmac(
...   'sha256', b'Password123', os.urandom(16), 100000
... )
>>> dk.hex()
'f8715c37906df067466ce84973e6e52a955be025a59c9100d9183c4cbec27a9e'
>>> hashlib.algorithms_available
{'SHA512', 'SHA256', 'shake_256', 'sha3_256', 'ecdsa-with-SHA1',
 'DSA-SHA', 'sha1', 'sha384', 'sha3_224', 'whirlpool', 'mdc2',
 'RIPEMD160', 'shake_128', 'MD4', 'dsaEncryption', 'dsaWithSHA',
 'SHA1', 'blake2s', 'md5', 'sha', 'sha224', 'SHA', 'MD5',
 'sha256', 'SHA384', 'sha3_384', 'md4', 'SHA224', 'MDC2',
 'sha3_512', 'sha512', 'blake2b', 'DSA', 'ripemd160'}
>>> hashlib.algorithms_guaranteed
{'blake2s', 'md5', 'sha224', 'sha3_512', 'shake_256', 'sha3_256',
 'shake_128', 'sha256', 'sha1', 'sha512', 'blake2b', 'sha3_384',
 'sha384', 'sha3_224'}

>>> import os
>>> h = hashlib.blake2b(
...   b'Important payload', digest_size=16, key=b'secret-key',
...   salt=b'random-salt', person=b'fabrizio'
... )
>>> h.hexdigest()
'c2d63ead796d0d6d734a5c3c578b6e41'
