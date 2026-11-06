"""本地 HTTP 练习服务。仅绑定 127.0.0.1，不需要真实网站账号。"""
import json
import threading
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlsplit

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def reply(self, data, code=200, content_type='application/json; charset=utf-8', cookie=None):
        body = data if isinstance(data, bytes) else json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlsplit(self.path)
        if url.path == '/robots.txt':
            self.reply(b'User-agent: *\nDisallow: /private\nAllow: /catalog\n', content_type='text/plain')
        elif url.path == '/private':
            ok = 'session=demo' in self.headers.get('Cookie', '')
            self.reply({'authorized': ok}, 200 if ok else 401)
        elif url.path == '/catalog':
            page = int(parse_qs(url.query).get('page', ['1'])[0])
            items = [{'id': (page-1)*2+i, 'title': f'课程{(page-1)*2+i}'} for i in (1, 2)]
            self.reply({'page': page, 'items': items})
        elif url.path == '/image':
            self.reply(b'<svg xmlns="http://www.w3.org/2000/svg" width="120" height="50"><text x="5" y="30">Python</text></svg>', content_type='image/svg+xml')
        elif url.path == '/media':
            self.reply(b'DEMO-MEDIA-BYTES', content_type='application/octet-stream')
        else:
            self.reply({'query': parse_qs(url.query), 'user_agent': self.headers.get('User-Agent'), 'method': 'GET'})

    def do_POST(self):
        data = self.rfile.read(int(self.headers.get('Content-Length', 0)))
        if self.path == '/login':
            self.reply({'login': 'demo'}, cookie='session=demo; HttpOnly; Path=/')
        else:
            try:
                payload = json.loads(data)
            except ValueError:
                payload = parse_qs(data.decode())
            self.reply({'method': 'POST', 'data': payload})

@contextmanager
def local_server():
    server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f'http://127.0.0.1:{server.server_port}'
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
