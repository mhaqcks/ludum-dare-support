from gevent.http import HTTPServer


def handle(request):
    print(dir(request))
    print(request.get_input_headers())
    data = request.get_input_headers()
    if request.uri == '/':
        request.add_output_header('Content-Type', 'text/html')
        request.send_reply(200, "OK", '')
    else:
        request.add_output_header('Content-Type', 'text/html')
        request.send_reply(404, "Not Found", "<h1>Not Found</h1>")

server = HTTPServer(('127.0.0.1', 12345), handle)

server.serve_forever()
