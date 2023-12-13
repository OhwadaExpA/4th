# coding: utf-8
# ソケット通信(サーバー側)
import socket
import csv
from datetime import datetime
from traceback import print_exc


DTFMT = '%Y-%m-%d %H:%M:%S'


# サーバーのIPアドレス
host_ip = 'localhost'  # ここを自分のノートPCのIPアドレスに書き換える
# ソケット通信で使用するTCPポート
port = 8765
# データ通信のバッファサイズ
datasize = 1024

# ソケット通信のおまじない
# IPv4のstreamソケット(TCP通信ソケット)を用意する
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# ソケットにIPアドレスとポート番号をバインド
server_socket.bind((host_ip, port))
# ソケットをリッスンさせる
server_socket.listen(1)
timestamp = datetime.now().strftime(DTFMT)
print("[{}]: Server has been initialized.".format(timestamp))

# クライアントソケットの初期化
client_socket = None

while True:
    # メッセージの初期化
    # 受信メッセージ: Union[None, str]
    recvline = None
    # 送信メッセージ: Union[None, str]
    sendline = None
    try:
        if client_socket is None:
            # コネクションとアドレスを取得
            # クライアントから接続されたらアクセプトする
            client_socket, address = server_socket.accept()
            timestamp = datetime.now().strftime(DTFMT)
            print('[{0}]: connect client -> address : {1}'.format(
                timestamp, address))

        # クライアントからデータを受信
        recvline = client_socket.recv(datasize).decode()
        timestamp = datetime.now().strftime(DTFMT)
        data = [timestamp, recvline]

        # 受信メッセージを送り返す
        sendline = recvline.encode('utf-8')
        client_socket.send(sendline)

        if recvline == 'exit':
            client_socket.close()
            client_socket = None
            continue

    except KeyboardInterrupt:
        print("キーボードインターラプトにより終了")
        break

    except Exception as e:
        print(e)
        print_exc()
        # クローズ
        if client_socket is not None:
            try:
                client_socket.close()
            except Exception:
                pass
        server_socket.close()
        exit(1)

    if recvline is not None and recvline != '':
        with open('./log.csv', mode='a', newline='') as f:
            w = csv.writer(f)
            w.writerow(data)
            print(data)
    else:
        break

# クローズ
if client_socket is not None:
    try:
        client_socket.close()
    except Exception:
        pass
server_socket.close()
print('サーバー側終了です')

