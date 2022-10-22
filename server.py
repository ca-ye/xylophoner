from http.server import BaseHTTPRequestHandler, HTTPServer

# the pi ip is 192.168.0.28, the computer ip is the same but instead of 26 at the end its 152

hostName = "192.168.0.152"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes(f"{f.read()}", "utf-8"))


if __name__ == "__main__":

    f = open("nevergonna.html", "r")

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName,serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
