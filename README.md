
# Shinji_SP
このプログラム名は前任のプログラムに倣っているだけで私の趣味ではありません。プログラムの使い方は書いてある通りですが、もし難しく感じたら遠慮なくTroubleのアドレスにメールください。

# Summary
和田研究室用のリポジトリです。ビデオ、慣性センサ（ロジカスプロダクト製品）、光学式モーションキャプチャーの同期を行うプログラムです。CUIプログラムなので少々使いづらいかと思いますが、GUIプログラムにする気力がなかったのでご容赦ください。GUIプログラムにしたければご勝手に改良して頂いてかまいません。

# Requirement
- opencv   >= 4.5.3
- pyserial >= 3.4


## インストール方法が分からない場合
以下のサイトからインストールコード（例：`pip install pyserial`）をコピーしてコマンドプロンプト上で実行してください。
- Anacondaでパッケージを管理しているあなたへ
  - [opencvはこちらのサイトにアクセス](https://anaconda.org/conda-forge/opencv)
  - [pyserialはこちらのサイトにアクセス](https://anaconda.org/anaconda/pyserial)
- pipでパッケージを管理しているあなたへ（Anacondaを知らない場合も）
  - [opencvはこちらのサイトにアクセス](https://pypi.org/project/opencv-python/)
  - [pyserialはこちらのサイトにアクセス](https://pypi.org/project/pyserial/)

# How to
1. git clone https://github.com/shinji1095/Shinji_SP.git
2. 研究室のArduino、慣性センサ、USBカメラをPCに接続
3. config.pyファイル内の設定に問題がないか確認
4. Requirementをインストール済みであることを確認
5. python Shinji_SP.py


# Trouble
分からないことがあればshinji1095nameko@gmail.comまでメールください。
