#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

def main():
    responses = 'HTTP/1.1 200\r\nX-Content-Type-Options: nosniff\r\nContent-Type: text/html;charset=UTF-8\r\n' \
                'Content-Language: zh-CN\r\nTransfer-Encoding: chunked\r\nDate: Thu, 29 Jun 2023 07:18:09 GMT\r\n' \
                'Keep-Alive: timeout=60\r\nConnection: keep-alive\r\n\r\n<!DOCTYPE html>\r\n<html>'

    response = responses.split('\r\n\r\n')

    response_partA = response[0].split('\r\n')

    print('ResponseLineParts: ')
    response_line_parts = response_partA[0].split(' ')
    protocol_version = response_line_parts[0]
    response_code = response_line_parts[1]
    print('ProtocolVersion: %s' % protocol_version)
    print('ResponseCode: %s' % response_code)
    print('----------------------')

    print('ResponseHeadersParts: ')
    response_headers = response_partA[1:]
    headers = {}
    for part in response_headers:
        key, value = part.split(": ", 1)
        headers[key] = value
        print("%s : %s" % (key, value))
    print('----------------------')

    print('ResponseBodyParts: \n')
    respinse_body = response[1]
    print(respinse_body)


if __name__ == '__main__':
    main()
