import jwt


data = {'payload': 'data', 'iss': 'fab', 'aud': 'learn-python'}


secret = 'secret-key'
token = jwt.encode(data, secret)


def decode(token, secret, issuer=None, audience=None):
    try:
        print(jwt.decode(
            token, secret, issuer=issuer, audience=audience))
    except (
        jwt.InvalidIssuerError, jwt.InvalidAudienceError
    ) as err:
        print(err)
        print(type(err))


decode(token, secret)

# not providing the issuer won't break
decode(token, secret, audience='learn-python')

# not providing the audience will break
decode(token, secret, issuer='fab')

# both will break
decode(token, secret, issuer='wrong', audience='learn-python')
decode(token, secret, issuer='fab', audience='wrong')

decode(token, secret, issuer='fab', audience='learn-python')


"""
$ python claims_auth.py
Invalid audience
<class 'jwt.exceptions.InvalidAudienceError'>

{'payload': 'data', 'iss': 'fab', 'aud': 'learn-python'}

Invalid audience
<class 'jwt.exceptions.InvalidAudienceError'>

Invalid issuer
<class 'jwt.exceptions.InvalidIssuerError'>

Invalid audience
<class 'jwt.exceptions.InvalidAudienceError'>

{'payload': 'data', 'iss': 'fab', 'aud': 'learn-python'}
"""
