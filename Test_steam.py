import asyncio
import websockets
import wave
import pyaudio

async def stream_audio(websocket, path):
    chunk = 1024
    wf = wave.open('c:\\euls\\ulaw.wav', 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    data = wf.readframes(chunk)
    while data:
        await websocket.send(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()

start_server = websockets.serve(stream_audio, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
