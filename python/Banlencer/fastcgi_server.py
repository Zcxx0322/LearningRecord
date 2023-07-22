#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps
#  FastCGI测试代码

from flup.server.fcgi import WSGIServer


# 定义一个处理请求的 WSGI 应用程序
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    body = b"Hello, World!"

    start_response(status, headers)
    return [body]


# 启动 FastCGI 服务器，绑定到本地的端口 9000
if __name__ == '__main__':
    WSGIServer(application, bindAddress=('localhost', 9000)).run()
