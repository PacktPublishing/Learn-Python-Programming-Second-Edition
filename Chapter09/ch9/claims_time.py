from datetime import datetime, timedelta
from time import sleep

import jwt


iat = datetime.utcnow()
nfb = iat + timedelta(seconds=1)
exp = iat + timedelta(seconds=3)


data = {'payload': 'data', 'nbf': nfb, 'exp': exp, 'iat': iat}


def decode(token, secret):
    print(datetime.utcnow().time().isoformat())
    try:
        print(jwt.decode(token, secret))
    except (
        jwt.ImmatureSignatureError, jwt.ExpiredSignatureError
    ) as err:
        print(err)
        print(type(err))


secret = 'secret-key'
token = jwt.encode(data, secret)


decode(token, secret)
sleep(2)
decode(token, secret)
sleep(2)
decode(token, secret)


"""
$ python claims_time.py
14:04:13.469778
The token is not yet valid (nbf)
<class 'jwt.exceptions.ImmatureSignatureError'>

14:04:15.475362
{'payload': 'data', 'nbf': 1522591454, 'exp': 1522591456, 'iat': 1522591453}

14:04:17.476948
Signature has expired
<class 'jwt.exceptions.ExpiredSignatureError'>
"""
