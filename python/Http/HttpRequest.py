#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

from urllib.parse import parse_qs, unquote


def split_request(http_message):
    http_up = http_message.split('\r\n\r\n')
    return http_up


def get_request_line(http_up):
    request_line_part = http_up[0].split('\r\n')
    request_line = request_line_part[0].split(' ')
    request_method = request_line[0]
    request_url = request_line[1]
    request_version = request_line[2]
    return request_method, request_url, request_version


def get_request_header(http_up):
    request_header_part = http_up[0].split('\r\n')
    request_header = request_header_part[1:]
    headers_str = ""

    for info in request_header:
        key, value = info.split(':', 1)
        key = key.strip()
        value = value.strip()
        headers_str += f"{key}: {value}\n"

    return headers_str


def get_body_main(http_lines):
    request_body = http_lines[-1]
    params = {}
    for param in request_body.split('&'):
        key, value = param.split('=')
        params[key] = value

    username = params.get('username', '')
    password = params.get('password', '')

    return username, password


def main():
    http_message = "POST /login HTTP/1.1\r\nHost: localhost:8080\r\nContent-Length: 129\r\n" \
                   "Content-Type: application/x-www-form-urlencoded\r\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64) " \
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36\r\n" \
                   "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp," \
                   "image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n" \
                   "Cookie: SESSION=MzEwNWVjMGQtNmI0Yy00NDIyLWI0OWMtMTUwMGRlOGUxMjQ3\r\n\r\n" \
                   "_csrf=da80f997-a389-4483-bac8-34d9812c72d6&username=3611744356%4@qq.com" \
                   "&password=0322&signin=%E9%A9%AC%E4%B8%8A%E7%99%BB%E5%BD%95"
    # 以\r\n切片
    http_lines = split_request(http_message)

    request_lines = get_request_line(http_lines)
    print("RequestMethod:", request_lines[0])
    print("RequestURL:", request_lines[1])
    print("ProtocolVersion:", request_lines[2])

    request_headers = get_request_header(http_lines)
    print(request_headers)

    http_body = split_request(http_message)
    print(http_body[1])

    print('-------------------------------------------')

    main_info = get_body_main(http_lines)
    print('Username:', main_info[0])
    print('Passworc:', main_info[1])


if __name__ == '__main__':
    main()
