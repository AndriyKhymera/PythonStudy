import socket
import os

basePath = os.getcwd()


def generate_list(**kwargs):
    page = '<ul >'
    for key in kwargs.keys():
        page += ("\t<li style =\"list-style: none\"><a href='{}'>{}</a></li>".format(key, kwargs[key]))
    page += '\n<ul>'
    return page


def generate_links(base, dirList):
    kwargs = {}
    currentPath = basePath + base
    for item in dirList:
        if (os.path.isdir(currentPath + "/" + item)):
            kwargs[base + "/"+ item] = item + "/"
        else:
            kwargs[base + "/" + item] = item
    return kwargs


def getResponse(request):
    header = str.split(request, "\n")[0]
    ref = str.split(header, " ")[1]

    newPath = basePath + ref

    http_response = ""
    if (ref == '/'):
        kwargs = generate_links("", os.listdir(basePath))
        links = generate_list(**kwargs)
        http_response = '\nHTTP/1.1 200 OK\n\n<a href="/">../</a {}'.format(links)
    elif (os.path.isdir(newPath)):
        kwargs = generate_links(ref, os.listdir(newPath))
        links = generate_list(**kwargs)
        http_response = '\nHTTP/1.1 200 OK\n\n<a href="{}">../</a {}'.format(os.path.split(ref)[0], links)
    else:
        try:
            if (not os.path.exists(newPath)):
                return "HTTP/1.1 200 OK"
            file = open(newPath, 'r')
            content = file.read()
            http_response = '\nHTTP/1.1 200 OK\n\n{}'.format(content)
            file.close()
        except (Exception):
            pass

    return http_response


HOST = ''
PORT = 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)

    print (request)
    http_response = getResponse(request)

    client_connection.sendall(http_response)
    client_connection.close()
