# auto_mahjong(音声認証で麻雀遊びする)

## 概要
【あとでまとめる】

## 事前準備
【あとでまとめる】

### pulseaudioのインストール
Windows版は、下記リンクの"zipfile containing preview binaries"のリンクから取得する。
https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/

### DBの準備
**[MongoDB](https://www.mongodb.com)使ってます。**

Try Freeで無料アカウント作ってReadWrite権限もっているユーザー(デフォで作られているもので可)をつくっておく。
- MAHJONG_DB_USER
- MAHJONG_DB_PASS
- MAHJONG_DB_CLUSTER

[上記の環境変数を利用して、DBアクセスURLを下記のように作ってます。](https://github.com/NIRANKEN/auto_mahjong/blob/main/app/dao/pymongo_client.py#L21-L23)
```
DB_ACCESS_URL="mongodb+srv://${MAHJONG_DB_USER}:${MAHJONG_DB_PASS}@${MAHJONG_DB_CLUSTER}.mongodb.net/myFirstDatabase"
```
### リソースの準備

画像認識用のファイル(下記参照)を`/resources`配下に入れてください。
`MAN1.png`や`REACH.png`などを作ってひたすら入れる感じです。
- https://github.com/NIRANKEN/auto_mahjong/blob/main/app/models/enums/mahjong_tiles.py
- https://github.com/NIRANKEN/auto_mahjong/blob/main/app/models/enums/mahjong_operations.py
- https://github.com/NIRANKEN/auto_mahjong/blob/main/app/models/enums/system_operations.py


## ユニットテスト
全部は書いてない。とりあえず枠組みだけ。
`python -m pytest tests`

## 注意事項
[WSL2でpyaudioが使えなかった](https://github.com/microsoft/WSL/issues/6818)ので、Windowsで実行確認した

requirements.txtのうち、pyaudioだけpipwinでインストールしている。
```
pip install pipwin
python -m pipwin install pyaudio
```

音声認証実行前にpulseaudio起動しておく。
`pulseaudio.exe --use-pid-file=false -D`

音声認証に利用するマイクは、default設定になっているもの(Windowsだとキャプチャ参照)
![image](https://user-images.githubusercontent.com/26358606/156390789-4a07237d-6a5d-4f4c-9b18-53c8ea5fcd06.png)
