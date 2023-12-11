# coding: utf-8
# ソケット通信(クライアント側)
import socket
from traceback import print_exc


# サーバーのIPアドレス
host_ip = 'localhost'  # ここをノートパソコンのIPアドレスに書き換える
# ソケット通信で使用するポート番号
port = 8765
server = (host_ip, port)
# 通信のバッファサイズ
datasize = 1024

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server)
except ConnectionRefusedError:
    print("サーバーが立ち上がっているか確認してください。")
    exit(1)

# 送信メッセージ
line = None

while line != 'exit':
    try:
        #  送信メッセージの初期化
        line = None  # Union[None, str]

        # [課題 以下を書き換える]
        # 標準入力からデータを取得
        print('メッセージを入力して下さい')
        line = input('>>>')
        # [課題 ここまで]

        if len(line) == 0:
            continue
        # サーバに送信
        server_socket.send(line.encode("UTF-8"))

        # サーバから受信
        recvdata = server_socket.recv(datasize).decode()
        # サーバから受信したデータを出力
        print('あなたが送ったメッセージは: ' + str(recvdata))
        if str(recvdata) != line:
            raise RuntimeError("送信したメッセージと受信メッセージが一致しません。")

    except KeyboardInterrupt:
        server_socket.send('exit'.encode("UTF-8"))
        _ = server_socket.recv(datasize).decode()
        print("キーボードインターラプト")
        break
    except Exception:
        try:
            server_socket.send('exit'.encode("UTF-8"))
            _ = server_socket.recv(datasize).decode()
        except Exception:
            print_exc()
        print_exc()

server_socket.close()
print('クライアント側終了です')

