#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

import uuid
import hashlib

# 用户信息
user_info = {
    'username': 'zcx',
    'password': 'zcx'
}

# 服务端的token存储，这里我们只用一个字典代替
token_store = {}


def create_token(user):
    # 生成一个随机的token
    raw_token = uuid.uuid4().hex
    # 可以使用hash函数进一步增加复杂性
    token_info = hashlib.md5(raw_token.encode('utf-8')).hexdigest()
    # 在服务端保存token和用户信息的关系
    token_store[token_info] = user
    return token_info


def verify_token(token_info):
    # 验证token是否存在于服务端的存储中
    if token_info in token_store:
        return token_store[token_info]
    else:
        print('Invalid token!')
        return None


if __name__ == '__main__':
    # 创建一个token
    token = create_token(user_info)
    print("Original Token: ", token)

    tampered_token = token[:-1]  # 删除最后一个字符
    print("Tampered Token: ", tampered_token)

    # 验证一个无效的token
    payload = verify_token(tampered_token)
    if payload:
        print("Token is valid! Payload: ", payload)
