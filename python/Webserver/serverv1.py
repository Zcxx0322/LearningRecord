import socketserver


# import base64


class MyTCPHandler(socketserver.BaseRequestHandler):
    data: bytes

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)

        # with open("/home/colamps/Pictures/test.jpeg", "rb") as f:
        #     image_data = f.read()

        response_html = """
        <html>
        <head><title>My Web Page</title></head>
        <body>
            <h1>Hello, World!</h1>
        </body>
        </html>
        """

        response = "HTTP/1.1 200 OK\r\n" \
                   "Content-Type: text/html; charset=utf-8\r\n" \
                   "Content-Length: {}\r\n".format(len(response_html))
        response += "\r\n"
        response += response_html
        # response = "HTTP/1.1 200 OK\r\n"
        # response += "Content-Type: image/jpeg\r\n"
        # response += "Content-Length: {}\r\n".format(len(image_data))
        # response += "\r\n"

        self.request.sendall(bytes(response, encoding='utf-8'))

        # self.request.sendall(image_data)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        print("Server is running on {}:{}".format(HOST, PORT))
        server.serve_forever()
