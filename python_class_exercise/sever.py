from wsgiref.simple_server import make_server
from app import application
httpd = make_server('',80,application)    
httpd.serve_forever()

# 然后可以直接访问127.0.0.1