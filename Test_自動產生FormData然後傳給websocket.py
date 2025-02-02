import asyncio
import websockets
import mimetypes
from aiohttp import FormData

async def generate_form_data(file_path):
    form = FormData()
    mime_type, _ = mimetypes.guess_type(file_path)
    mime_type = mime_type or 'application/octet-stream'

    with open(file_path, 'rb') as file:
        form.add_field('file', file, filename=file_path, content_type=mime_type)
    
    # Extract the payload from FormData
    form_data = form()
    payload = b''
    async for chunk in form_data.iter_chunks():
        payload += chunk
    return payload

async def send_form_data_via_websocket(uri, file_path):
    form_data = await generate_form_data(file_path)

    async with websockets.connect(uri) as websocket:
        await websocket.send(form_data)
        response = await websocket.recv()
        print(f"Received response: {response}")

async def main():
    uri = "ws://your.websocket.server/endpoint"
    file_path = "path/to/your/file.txt"
    await send_form_data_via_websocket(uri, file_path)

if __name__ == "__main__":
    asyncio.run(main())



'''
import aiohttp
import asyncio
import websockets
from aiohttp import FormData

async def send_form_data_via_websocket(file_path):
    # 創建 FormData 並添加文件
    form = FormData()
    form.add_field('file',
                   open(file_path, 'rb'),
                   filename=file_path,
                   content_type='application/octet-stream')

    # 使用 aiohttp 發送請求來生成 multipart/form-data
    async with aiohttp.ClientSession() as session:
        async with session.post('http://httpbin.org/post', data=form) as resp:
            data = await resp.read()

    # 使用 websockets 發送數據
    uri = "ws://your.websocket.server/endpoint"
    async with websockets.connect(uri) as websocket:
        await websocket.send(data)

async def main():
    file_path = 'path/to/your/file.txt'
    await send_form_data_via_websocket(file_path)

if __name__ == "__main__":
    asyncio.run(main())
'''