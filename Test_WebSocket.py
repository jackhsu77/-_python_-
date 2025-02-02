import websocket    # pip install websocket-client

def on_open(ws):
    print("Connection opened")
    ws.send("Hello, WebSocket server!")
def on_close(ws, p2, p3):                   # 會有3個參數回傳, 若沒有給p2, p3去收則會發生錯誤
    print("Connection closed")
    print(p2, p3)
def on_error(ws, error):                    # 把Server關閉, 則on_error就會引發10054錯誤
    print(f"Error: {error}")
def on_message(ws, message):
    print(f"Received message: {message}")


if __name__ == "__main__":
    print("web socket start...")
    #websocket.enableTrace(True)
    # 位址為C#的websocketServer伺服器測試程式設定的
    ws = websocket.WebSocketApp("ws://127.0.0.1:5000/notify",      # ok
    #ws = websocket.WebSocketApp("ws://192.168.50.52:5000/notify",   # ok
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    print("web socket 1...")
    ws.on_open = on_open
    print("web socket 2...")
    for i in range(5):
        try:
            print(f"{i+1}: run_forever")
            ws.run_forever()
        except Exception as e:
            print("run_forever: " + str(e))
    
    print("web socket end...")
    exit()
