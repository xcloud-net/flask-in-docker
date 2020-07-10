import jwt
from flask import request, current_app
from functools import wraps
import requests
import json
from jwt.algorithms import get_default_algorithms

jwk_uri = 'https://agilewater.cn:5001/.well-known/openid-configuration/jwks'


def get_jwk():
    try:
        with requests.get(jwk_uri) as res:
            data = res.content.decode('utf-8')
            key = json.loads(data)['keys'][0]
            json_data = json.dumps(key, ensure_ascii=False)
            return json_data
    except Exception as e:
        print(e)


def login_required(func):
    '''
    这里可以直接解析jwt也可以调用接口获取用户信息
    :param func:
    :return:
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(request)
        request.user = {
            'is_authenticated': False,
            'message': '没有登陆'
        }
        try:
            token = request.headers.get('Authorization', '').split(' ')[1]

            key = current_app.config['jwk_key']
            assert key is not None
            print(key)
            rsa = get_default_algorithms()['RS256']
            # 必须安装cryptography才会有from jwk这个方法
            cert = rsa.from_jwk(key)
            result = jwt.decode(token, cert, algorithms=['RS256'], audience='water')
            request.user = result
        except Exception as e:
            print(e)
        ret = func(*args, **kwargs)
        return ret

    return wrapper
