#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

import jwt

Login = {
    'username': 'zcx',
    'password': 'zcx'
}

# 秘钥
SECRET_KEY = "secret_key"
WRONG_KEY = "wrong_key"


def create_token() -> str:
    # 生成token
    token_data = jwt.encode(Login, SECRET_KEY, algorithm="HS256")
    return token_data


# def verify_token(token: str) -> dict:
#     # 用错误的密钥解码token
#     try:
#         payload_info = jwt.decode(token, WRONG_KEY, algorithms="HS256")
#         return payload_info
#     except jwt.InvalidTokenError:
#         print("Invalid token!")
#         return {}

def verify_token(token_data: str) -> dict:
    # 用正确的密钥解码token
    try:
        payload_info = jwt.decode(token_data, SECRET_KEY, algorithms="HS256")
        return payload_info
    except jwt.InvalidTokenError:
        print("Invalid token!")
        return {}


if __name__ == '__main__':
    # 创建一个token
    token = create_token()
    print("Generated Token: ", token)

    # 使用错误的秘钥验证token
    payload = verify_token(token)
    if payload:
        print("Token is valid! Payload: ", payload)
