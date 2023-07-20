#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps
from urllib.parse import urlparse
from urllib.parse import parse_qs

url = 'https://www.example.com/some_path?token=something'
parsed_url = urlparse(url)
print(parsed_url)
token_list = parse_qs(parsed_url.query)['token']
token = token_list[0]

print(token)
