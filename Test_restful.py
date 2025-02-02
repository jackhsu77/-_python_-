#!/usr/bin/env python

import os
import sys
import json

print("1223")
sys.exit()

# 設定標頭 (content-type: application/json)
print("Content-Type: application/json")
print()

# 獲取 HTTP 請求方法和路徑
method = os.environ.get('REQUEST_METHOD')
path_info = os.environ.get('PATH_INFO', '')

# 簡單路由邏輯
def handle_get():
    if path_info == '/api/v1/resource':
        response = {
            'message': 'This is a GET request for the resource'
        }
    else:
        response = {
            'error': 'Resource not found'
        }
    return json.dumps(response)

def handle_post():
    try:
        content_length = int(os.environ.get('CONTENT_LENGTH', 0))
        post_data = sys.stdin.read(content_length)
        data = json.loads(post_data)
        response = {
            'message': 'Data received',
            'data': data
        }
    except Exception as e:
        response = {
            'error': str(e)
        }
    return json.dumps(response)

# 根據請求方法處理
if method == 'GET':
    print(handle_get())
elif method == 'POST':
    print(handle_post())
else:
    print(json.dumps({'error': 'Method not allowed'}))
