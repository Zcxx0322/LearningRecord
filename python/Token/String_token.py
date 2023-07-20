#  !/home/colamps/workspace/pythonProject/test
#  -*- coding:utf8 -*-
#  Copyright(C) 2023-2024 colamps

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

RealToken = "zcx0322"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析URL和查询参数
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        # 检查token参数
        token_list = query_params.get('token', [None])
        token = token_list[0]

        if not token:
            # 未输入?token参数时返回资源
            self.send_error(400, "Missing token")
        elif token != RealToken:
            # 输入?token参数但错误时返回资源
            self.send_error(403, "Invalid token")
        else:
            # 正确输入token参数时返回资源
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'HelloWorld!')


if __name__ == '__main__':
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server Adress: http://localhost:8000")
    httpd.serve_forever()
