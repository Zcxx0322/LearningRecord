#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

def split_respinses(http_message):
    http_all = http_message.split('\r\n\r\n')
    return http_all


def get_response_line(http_split):
    response_line_part = http_split[0].split('\r\n')
    response_line = response_line_part[0].split(' ')
    response_version = response_line[0]
    response_code = response_line[1]
    return response_version, response_code


def get_response_header(http_split):
    response_header_part = http_split[0].split('\r\n')
    response_header = response_header_part[1:]
    headers_str = ""

    for info in response_header:
        key, value = info.split(':', 1)
        key = key.strip()
        value = value.strip()
        headers_str += f"{key}: {value}\n"

    return headers_str


def get_body_main(http_split):
    response_body = http_split[-1]
    return response_body


def main():
    http_message = 'HTTP/1.1 200\r\nX-Content-Type-Options: nosniff\r\nContent-Type: text/html;charset=UTF-8\r\n' \
                   'Content-Language: zh-CN\r\nTransfer-Encoding: chunked\r\nDate: Thu, 29 Jun 2023 07:18:09 GMT\r\n' \
                   'Keep-Alive: timeout=60\r\nConnection: keep-alive\r\n\r\n<!DOCTYPE html>\r\n<html>'

    http_split = split_respinses(http_message)

    request_lines = get_response_line(http_split)
    print("ProtocolVersion:", request_lines[0])
    print("Code:", request_lines[1])

    response_headers = get_response_header(http_split)
    print(response_headers)

    http_body = get_body_main(http_split)
    print(http_body)


if __name__ == '__main__':
    main()
