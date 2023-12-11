# 第4回 実験A IoTプログラミング

[ダウンロードリンク](https://github.com/OhwadaExpA/4th/archive/refs/tags/v1.0.zip)

## コンテンツ

- `server.py`: 自分のノートパソコンで動かすプログラム
- `client.py`: ラズパイ上で動かすプログラム

## 実行方法

### 準備

- ラズパイを立ち上げる
- 上のダウンロードリンクからコードをダウンロードして、解凍する。

### Step 1. 自分のノートパソコンのIPアドレスを調べる

#### Windowsの場合

PowerShellを立ち上げ、`ipconfig`と打つ。

```
PS C:\Users\m1cr0> ipconfig
```

出力の中から`Wireless LAN adapter WIFI:`という項目を見つける。

その中の`IPv4 アドレス`がノートパソコンのIPアドレス。

```
Wireless LAN adapter WIFI::

   接続固有の DNS サフィックス . . . . .:
   ...
   IPv4 アドレス . . . . . . . . . . . .: 192.168.x.x  <-- これ
   ...
```

#### MacOS, Linuxの場合

ここでは説明を省略します。詳しくはTAに聞いてください。

### Step 2. client.pyをラズパイに送る

#### Windowsの場合

1. ラズパイに接続しているTera Termを開く。
2. ファイル -> SSH SCPを選択
3. `Send`の左にある`・・・`を選択し、Explorerでダウンロードした`client.py`を指定。
4. `Send`を選択。

#### MacOS, Linuxの場合

ターミナルを開き、以下のコマンドを実行

```
scp /ダウンロードしたパス/client.py pi@ラズパイのipアドレス:/home/pi/
```

### Step 3. server.pyの起動

VSCodeを開く。

1. 上のリボンメニューから`ファイル`または`File`を選択
2. `ファイルを開く`からダウンロードした`server.py`を選択
3. `server.py`内13行目の`host_ip = 'localhost'`の`localhost`をStep1で調べたノートパソコンのIPアドレスに変更
4. F5キーを押して実行

＊4が上手くいかない人はTAに聞いてください。

### Step 4. client.pyを起動

#### Windowsの場合

1. ラズパイに接続しているTera Termを開く。
2. `nano client.py`で`client.py`内8行目の`host_ip = 'localhost'`の`localhost`をStep1で調べたノートパソコンのIPアドレスに変更
3. `nano`上で保存、終了
4. `python3 client.py`を実行

＊実行後、何も表示されないなど何らかの不具合がある場合はTAに聞いてください。

#### MacOS, Linuxの場合

1. ターミナルを開く。
2. `ssh pi@ラズパイのアドレス`でラズパイに接続
3. `nano client.py`で`client.py`内8行目の`host_ip = 'localhost'`の`localhost`をStep1で調べたノートパソコンのIPアドレスに変更
4. `nano`上で保存、終了
5. `python3 client.py`を実行
