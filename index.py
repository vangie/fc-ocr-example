# -*- coding: utf-8 -*-
import logging
import tesserocr
import cgi
import json
from PIL import Image
import requests
from io import BytesIO
import re

def handler(environ, start_response):
    context = environ['fc.context']
    request_uri = environ['fc.request_uri']
    request_method = environ['REQUEST_METHOD']
    path_info = environ['PATH_INFO']
    params = cgi.parse_qs(environ.get('QUERY_STRING', ''),
                          keep_blank_values=True)

    # 如果不是以 "/" 结尾的请求加上 "/"
    if path_info == '/' and not request_uri.endswith('/'):
        status = '301'
        response_headers = [('Location', request_uri + '/')]
        start_response(status, response_headers)
        return []
    # 返回示例图片
    elif re.match(r"/sample[1-3].jpg", path_info):
        status = '200 OK'
        response_headers = [
            ('context-type', 'image/jpeg')
        ]
        start_response(status, response_headers)
        f = open('/code/samples/%s' % path_info[1:], 'rb')
        return iter(lambda: f.read(128), ''.encode())
    # 处理图片识别请求
    elif path_info == '/recognize' and request_method == 'POST':
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True
        )
        type = form['type'].value
        api = tesserocr.PyTessBaseAPI()
        text = None
        error = None
        # 处理示例图片
        if type == 'sample':
            sample = form['sample'].value
            api.SetImageFile("samples/%s" % sample)
            text = api.GetUTF8Text()
        # 处理上传图片
        elif type == 'upload':
            fileItem = form['upload']
            image = Image.open(fileItem.file)
            text = tesserocr.image_to_text(image)
        # 处理图片 URL
        elif type == 'url':
            url = form['url'].value
            try:
                response = requests.get(url)
                image = Image.open(BytesIO(response.content))
                text = tesserocr.image_to_text(image)
            except Exception as e:
                if hasattr(e, 'message'):
                    error = e.message
                else:
                    error = str(e)

        response_headers = [('Content-type', 'application/json')]

        if error:
            start_response('500 Internal Error', response_headers)
            return [json.dumps({"code": 500, "error": error}).encode()]
        else:
            start_response('200 OK', response_headers)
            return [json.dumps({"code": 200, "text": text}).encode()]
    # 返回首页 index.html
    else:
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        f = open("index.html", "r")
        return iter(lambda: f.readline().encode(), ''.encode())