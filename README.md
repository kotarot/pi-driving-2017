# 議事録


## 2017年5月30日

ラジコン2種類組み立てた。

動画: [2017-05-30 14.57.06.mov](https://www.dropbox.com/s/bva3acwf8ktonle/2017-05-30%2014.57.06.mov?dl=0)


## 2017年5月19日

秋葉原に買い物行った。


## 2017年5月9日

Raspberry Pi カメラモジュールを動かしてみた。

* Raspberry Pi 3でネットワーク ライブカメラを構築する方法 Motion編 (ラズパイのカメラで遠隔監視カメラ（ネットワークカメラ、ライブカメラ）) http://www.neko.ne.jp/~freewing/raspberry_pi/raspberry_pi_3_camera_motion/

を参考にして `motion-mmal` をインストールして、

* Raspberry Pi motion-mmalのインストールと起動 https://arakan60.mydns.jp/04kousaku/22-01motionml.html

を参考にして、静止画の撮影 (`raspistill`) とリアルタイムライブ映像 (`motion-mmal`) をウェブブラウザを経由して見られるようになった。
`raspistill` ではオプションを指定すると画像加工できることがわかった。

静止画を撮影するコマンドを前回作成した [drive.py](/drive.py) に組み込んで、
コントローラーのボタンを押すと、ボタンの種類に応じて加工された静止画を撮影することができた。


## 2017年4月25日

PS4のコントローラーのデータを取得した。
Pygameライブラリを用いる。
サンプルプログラム [joystick.py](/joystick.py) を参考に
[drive.py](/drive.py) を作成した。

コントローラの接続のやり方:
```
sudo ds4drv
```
ここでSHAREボタンとPSボタンを長押しする (白いライトが点滅する)。
接続後、Pythonプログラムを実行する。
```
python3 drive.py
```


## 2017年4月18日

決まったこと。

### 入力
PS4コントローラ。  
だめなら、スマホ。

### やること
カメラでスマホ。

### できたらやること
スタートボタンでスタート地点に戻る。

### 買い物の日程
秋葉原買い物は一緒に行く。  
5月19日(金) 13時 戸川研集合。
