import signal
import socketserver


# noinspection PyUnusedLocal
def sigint_handler(sig, frame):
    print('\n\n收到 Ctrl+C 信号，退出......')
    exit(0)


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        # just send back the same data, but upper-cased
        self.request.sendall(data.upper())


def main():
    host, port = "localhost", 9999

    server = socketserver.TCPServer(server_address=(host, port),
                                    RequestHandlerClass=MyTCPHandler,
                                    bind_and_activate=False)

    # 设置socket参数
    server.allow_reuse_address = True
    server.allow_reuse_port = True

    # 在没有设置socket参数前，不能监听端口
    server.server_bind()
    server.server_activate()

    server.serve_forever()


if __name__ == "__main__":
    # 前台运行收到 CTRL+C 信号，直接退出。
    signal.signal(signal.SIGINT, sigint_handler)

    main()