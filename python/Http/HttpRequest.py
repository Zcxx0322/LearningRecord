#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps


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
    http_lines = http_message.split('\r\n')

    # 处理请求行
    print('-------------')
    print("Request Line")

    request_line_parts = http_lines[0].split(' ')
    request_method = request_line_parts[0]
    request_url = request_line_parts[1]
    protocol_version = request_line_parts[2]
    print("Method: %s" % request_method)
    print("Url: %s" % request_url)
    print("Version: %s" % protocol_version)

    headers = {}
    for line in http_lines[1:]:
        if line == '':
            break
        key, value = line.split(': ')
        headers[key] = value

    print('-------------')
    print("Headers:")
    for key, value in headers.items():
        print("%s : %s" % (key, value))

    request_body = http_lines[-1]
    params = {}
    for param in request_body.split('&'):
        key, value = param.split('=')
        params[key] = value

    print('-------------')
    print("Body:")
    print("Username: %s" % params['username'])
    print("Password: %s" % params['password'])


if __name__ == '__main__':
    main()
