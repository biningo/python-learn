import json

from wsgiref.simple_server import make_server
def hello(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-Type', 'application/json')]
    start_response(status, response_headers) #这是一个可调用的回调函数
    # path = environ['PATH_INFO'][1:] or 'hello'
    data={"name":"biningo","age":18}
    print(environ["PATH_INFO"]) #获取访问路径
    return [bytes(json.dumps(data),encoding='utf-8')]

if __name__ == '__main__':
    server = make_server('localhost', 8000, hello)
    print('Serving HTTP on port 8000...')
    server.serve_forever()

